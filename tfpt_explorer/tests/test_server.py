import json
import threading
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from urllib.parse import urlsplit

import pytest

from tfpt_explorer.server import ROOT, create_server, run_pipeline, validate_config


def test_whole_pipeline_keeps_typed_links_and_returns_real_outputs():
    result = run_pipeline()
    assert len(result["stages"]) == 24
    failures = [(stage["id"], check) for stage in result["stages"]
                for check in stage["checks"] if not check["ok"]]
    assert result["summary"]["failed"] == 0, failures
    stages = {s["id"]: s for s in result["stages"]}
    assert stages["e8"]["data"]["glue_coset_sizes"] == [52, 64, 60, 64]
    assert stages["seam"]["data"]["homology_rank"] == 3
    assert len(stages["e8"]["data"]["roots"]) == 240
    assert stages["observability"]["data"]["closure_ranks"] == [10, 20, 25]
    assert len(result["tour"]["chapters"]) == 15
    assert result["tour"]["chapters"][10]["visual"]["data"]["stages"] == stages["normalization"]["data"]
    for edge in result["edges"]:
        assert edge["source"] in stages and edge["target"] in stages
        assert edge["relation"] in {"derives", "feeds", "assumes", "checks", "corresponds"}
    for stage in stages.values():
        for source in stage["sources"]:
            if "url" in source:
                parsed = urlsplit(source["url"])
                assert parsed.scheme == "https" and parsed.hostname
            else:
                assert (ROOT / source["path"]).is_file()
    json.dumps(result, allow_nan=False)


@pytest.mark.parametrize("config", [{"clock_step": float("nan")}, {"phase_b": float("inf")}, {"efolds": True}, {"transfer_steps": 41}, {"recursion_depth": 0}, {"initial_state": "coherent"}, {"command": "echo injected"}])
def test_invalid_or_unknown_controls_rejected(config):
    with pytest.raises((ValueError, OverflowError)):
        validate_config(config)


@pytest.fixture
def local_server():
    server = create_server(0)
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    yield server, f"http://127.0.0.1:{server.server_port}"
    server.shutdown()
    server.server_close()
    worker.join(timeout=2)


def test_source_reader_preserves_repository_boundary_and_only_registered_sources(local_server):
    server, url = local_server
    for path in ("/api/source?path=../../.ssh/id_rsa", "/api/source?path=AGENTS.md"):
        with pytest.raises(HTTPError) as exc:
            urlopen(url + path)
        assert exc.value.code == 403
    server.state.allowed_sources.add("tfpt_explorer/core.py")
    source = json.load(urlopen(url + "/api/source?path=tfpt_explorer/core.py&line=1"))
    assert source["path"] == "tfpt_explorer/core.py"
    assert "Canonical calculation" in source["text"]


def test_external_origin_cannot_start_local_execution(local_server):
    _, url = local_server
    request = Request(url + "/api/run", data=b'{}', method="POST", headers={"Content-Type": "application/json", "Origin": "https://unrelated.example"})
    with pytest.raises(HTTPError) as exc:
        urlopen(request)
    assert exc.value.code == 403


def test_live_source_word_uses_original_mixed_field_rule(local_server):
    _, url = local_server
    word = [{"kind": "X", "i": i, "a": a, "dagger": dagger}
            for i, a, dagger in [(0, 0, False), (1, 0, True), (1, 1, False),
                                (2, 1, True), (2, 2, False), (0, 2, True)]]
    def post(positions):
        return urlopen(Request(url + "/api/source-word", method="POST",
                               data=json.dumps({"word": word, "positions": positions}).encode(),
                               headers={"Content-Type": "application/json"}))
    result = json.load(post([-5, -2, -1, 1, 3, 7]))
    assert result["value_exact"] == result["connected_value_exact"] == "1/576"
    with pytest.raises(HTTPError) as exc:
        post([-5, -2, -1, 1, 3, 3])
    assert exc.value.code == 400


def test_live_source_word_rejects_unbounded_exponent_notation(local_server):
    _, url = local_server
    payload = {"word": [{"kind": "C", "a": 0}, {"kind": "C", "a": 0, "dagger": True}],
               "positions": [0, "1e-100000000"]}
    request = Request(url + "/api/source-word", method="POST", data=json.dumps(payload).encode(),
                      headers={"Content-Type": "application/json"})
    with pytest.raises(HTTPError) as exc:
        urlopen(request)
    assert exc.value.code == 400


def test_pdf_page_preview_keeps_original_and_registered_source_boundary(local_server, monkeypatch, tmp_path):
    from tfpt_explorer import pdf_preview
    server, url = local_server
    source = "tfpt_explorer/sources/TFPT_Konsolidierung_20260928.pdf"
    route = "/source?path=" + source
    image = tmp_path / "page.png"
    image.write_bytes(b"\x89PNG\r\n\x1a\n")
    calls = []

    def preview(path, page, cache):
        calls.append((path, page))
        if page < 1 or page > 68:
            raise ValueError("Seite außerhalb des Dokuments")
        return image, 68, "testhash"

    monkeypatch.setattr(pdf_preview, "page_preview", preview)
    with pytest.raises(HTTPError) as exc:
        urlopen(url + route + "&page=25")
    assert exc.value.code == 403
    assert calls == []
    server.state.allowed_sources.add(source)
    page = urlopen(url + route + "&page=25").read().decode()
    assert "PDF-Seite 25 von 68" in page and "render=image" in page
    response = urlopen(url + route + "&page=25&render=image")
    assert response.headers["Content-Type"] == "image/png"
    assert response.read() == image.read_bytes()
    assert urlopen(url + route).read() == (ROOT / source).read_bytes()
    with pytest.raises(HTTPError) as exc:
        urlopen(url + route + "&page=69")
    assert exc.value.code == 400


def test_http_defaults_catalog_loading_and_invalid_run(local_server):
    _, url = local_server
    assert json.load(urlopen(url + "/api/state"))["defaults"]["phase_b"] == 1 / 18
    response = urlopen(url + "/api/catalog")
    assert response.status == 202
    assert json.load(response)["loading"] is True
    request = Request(url + "/api/run", data=b'{"config":{"phase_b":9}}', method="POST", headers={"Content-Type": "application/json"})
    with pytest.raises(HTTPError) as exc:
        urlopen(request)
    assert exc.value.code == 400
