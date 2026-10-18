/**
 * In-browser Python runtime for the live reproducer.
 *
 * Browser-compatible verification scripts are the project's own deterministic
 * code and run client-side inside the Pyodide WebAssembly sandbox (no server,
 * no machine access, no user input is executed). A small, explicit native-only
 * set uses libraries that Pyodide does not provide and is routed to the local
 * reproduction command instead of being presented as a browser certificate.
 */

const PYODIDE_VERSION = "0.29.4";
const INDEX_URL = `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/`;
const WORK_DIR = "/home/pyodide";

const NATIVE_ONLY_SCRIPTS: Record<string, string> = {
  "v1022_telb_round3_certificates.py":
    "This interval certificate requires native python-flint==0.9.0 (Arb/Acb) and is not reproducible in Pyodide. Run the local command below in the repository environment.",
  "v1025_telb_c1_c2a_certificates.py":
    "This interval certificate requires native python-flint==0.9.0 (Arb/Acb) and is not reproducible in Pyodide. Run the local command below in the repository environment.",
  "v1026_telb_round4_closure.py":
    "This interval certificate requires native python-flint==0.9.0 (Arb/Acb) and is not reproducible in Pyodide. Run the local command below in the repository environment.",
  "v1033_charged_disorder.py":
    "This checker reads the original QWZ builder and MMST article from the complete repository. Those source inputs are not mounted in the browser sandbox. Run the local command below from a full checkout.",
  "v1034_parent_mirror.py":
    "This checker audits the original parent and mirror source files from the complete repository. Those source inputs are not mounted in the browser sandbox. Run the local command below from a full checkout.",
};

/** These checks inspect complete paper/research sources, which are not mounted here. */
const SOURCE_CONTEXT_SCRIPTS = new Set([
  "v188_frontier_wording_guard.py", "v265_qft4d_fork_freeze.py",
  "v649_discipline_audit.py", "v1006_mmst_lemma_battery.py",
  "v1007_det16_stability_battery.py", "v1013_thermodynamic_dynamics.py",
  "v1014_bridge_refinements.py", "v1015_axiom_core_closure.py",
  "v1016_state_gap_batteries.py", "v1033_charged_disorder.py",
]);

// eslint-disable-next-line @typescript-eslint/no-explicit-any
type Pyodide = any;

declare global {
  interface Window {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    loadPyodide?: (opts: { indexURL: string }) => Promise<Pyodide>;
  }
}

let pyodidePromise: Promise<Pyodide> | null = null;
const scriptCache = new Map<string, string>();

function loadScriptOnce(src: string): Promise<void> {
  return new Promise((resolve, reject) => {
    if (document.querySelector(`script[data-pyodide]`)) {
      resolve();
      return;
    }
    const s = document.createElement("script");
    s.src = src;
    s.async = true;
    s.dataset.pyodide = "true";
    s.onload = () => resolve();
    s.onerror = () => reject(new Error("Failed to load the Pyodide runtime."));
    document.head.appendChild(s);
  });
}

async function fetchText(path: string): Promise<string> {
  const cached = scriptCache.get(path);
  if (cached) return cached;
  const res = await fetch(path);
  if (!res.ok) throw new Error(`Could not fetch ${path} (${res.status}).`);
  const text = await res.text();
  scriptCache.set(path, text);
  return text;
}

type StatusFn = (s: string) => void;

/** Lazily boot Pyodide once and pre-load the shared constants module. */
async function getPyodide(onStatus?: StatusFn): Promise<Pyodide> {
  if (!pyodidePromise) {
    pyodidePromise = (async () => {
      onStatus?.("Loading the Python runtime (Pyodide, ~once)…");
      await loadScriptOnce(`${INDEX_URL}pyodide.js`);
      if (!window.loadPyodide) throw new Error("Pyodide failed to initialise.");
      const py = await window.loadPyodide({ indexURL: INDEX_URL });

      onStatus?.("Loading the shared constants (tfpt_constants.py)…");
      const consts = await fetchText("/verification/tfpt_constants.py");
      py.FS.writeFile(`${WORK_DIR}/tfpt_constants.py`, consts);
      const texSources = await fetchText("/verification/tex_sources.py");
      py.FS.writeFile(`${WORK_DIR}/tex_sources.py`, texSources);
      // tfpt_constants imports mpmath at module level → make sure it is present.
      await py.loadPackagesFromImports(consts);
      py.runPython(`import sys\nif ${JSON.stringify(WORK_DIR)} not in sys.path: sys.path.insert(0, ${JSON.stringify(WORK_DIR)})`);
      return py;
    })();
  }
  return pyodidePromise;
}

export interface CheckRow {
  ok: boolean;
  label: string;
}

export interface RunResult {
  header: string;
  checks: CheckRow[];
  passed: number;
  failed: number;
  ok: boolean;
  raw: string;
  error?: string;
}

export function nativeRuntimeNote(file: string): string | null {
  return NATIVE_ONLY_SCRIPTS[file] ?? (SOURCE_CONTEXT_SCRIPTS.has(file)
    ? "This checker reads the complete modular LaTeX or research sources. Those inputs are not mounted in the browser sandbox. Run it from a full repository checkout to preserve its document checks."
    : null);
}

function parseOutput(raw: string): Omit<RunResult, "raw" | "error"> {
  const lines = raw.split("\n");
  const checks: CheckRow[] = [];
  let header = "";
  let passed = 0;
  let failed = 0;
  for (const line of lines) {
    const m = line.match(/^\s*\[(PASS|FAIL)\]\s+(.*)$/);
    if (m) {
      checks.push({ ok: m[1] === "PASS", label: m[2].trim() });
      continue;
    }
    const sum = line.match(/---\s+.*?:\s+(\d+)\s+passed,\s+(\d+)\s+failed\s+---/);
    if (sum) {
      passed = parseInt(sum[1], 10);
      failed = parseInt(sum[2], 10);
      continue;
    }
    if (!header && line.trim() && !line.includes("[")) header = line.trim();
  }
  if (passed === 0 && failed === 0) {
    passed = checks.filter((c) => c.ok).length;
    failed = checks.filter((c) => !c.ok).length;
  }
  return { header, checks, passed, failed, ok: failed === 0 && checks.length > 0 };
}

/**
 * Run a browser-compatible verification script and return its parsed output.
 * Native-only certificates return an explicit local-runtime result before
 * Pyodide is loaded; they never produce a synthetic browser PASS.
 */
/** Extra data files a script reads from its own directory at runtime. */
const SCRIPT_ASSETS: Record<string, string[]> = {
  "v84_frozen_registry.py": ["predictions_frozen.json"],
  "v100_numerology_null_mc.py": ["predictions_frozen.json"],

};

export async function runScript(
  file: string,
  onStatus?: StatusFn,
): Promise<RunResult> {
  const nativeOnly = nativeRuntimeNote(file);
  if (nativeOnly) {
    return {
      header: "Local repository verification",
      checks: [],
      passed: 0,
      failed: 0,
      ok: false,
      raw: "",
      error: nativeOnly,
    };
  }

  const py = await getPyodide(onStatus);
  onStatus?.(`Fetching ${file}…`);
  const src = await fetchText(`/verification/${file}`);
  py.FS.writeFile(`${WORK_DIR}/${file}`, src);
  for (const asset of SCRIPT_ASSETS[file] ?? []) {
    const data = await fetchText(`/verification/${asset}`);
    py.FS.writeFile(`${WORK_DIR}/${asset}`, data);
  }

  onStatus?.("Resolving packages (numpy, sympy, mpmath, scipy…)…");
  await py.loadPackagesFromImports(src);

  onStatus?.("Running the script…");
  const modname = file.replace(/\.py$/, "");
  // Capture stdout/stderr deterministically into a StringIO (newlines intact),
  // instead of relying on the per-line `batched` callback.
  const code = [
    "import importlib, sys, io, contextlib, traceback",
    "import tfpt_constants as _tc",
    "_tc.reset()",
    `sys.modules.pop(${JSON.stringify(modname)}, None)`,
    "_buf = io.StringIO()",
    "_err = ''",
    "with contextlib.redirect_stdout(_buf), contextlib.redirect_stderr(_buf):",
    "    try:",
    `        _m = importlib.import_module(${JSON.stringify(modname)})`,
    "        if hasattr(_m, 'run'):",
    "            _m.run()",
    "    except Exception:",
    "        _err = traceback.format_exc()",
    "_out = _buf.getvalue()",
  ].join("\n");

  let raw = "";
  let error: string | undefined;
  try {
    py.runPython(code);
    raw = String(py.globals.get("_out") ?? "");
    const err = String(py.globals.get("_err") ?? "");
    if (err.trim()) error = err;
  } catch (e) {
    error = e instanceof Error ? e.message : String(e);
  }

  const parsed = parseOutput(raw);
  return { ...parsed, raw, ok: error ? false : parsed.ok, error };
}

export function pyodideVersion() {
  return PYODIDE_VERSION;
}
