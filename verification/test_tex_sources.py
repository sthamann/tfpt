"""Focused regressions for transparent, source-attributed TeX include reading."""
from pathlib import Path
import tempfile
import unittest
from tex_sources import read_tex, source_chunks, MissingTexSourceError, TexIncludeCycleError, dependency_paths


class TexSourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def put(self, path, text):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode('utf-8'))
        return p

    def test_nested_order_and_no_invented_whitespace(self):
        root = self.put('main.tex', 'A\\input{part}Z')
        self.put('part.tex', 'B\\include{nested}C')
        self.put('nested.tex', 'D')
        self.assertEqual(read_tex(root), 'ABDCZ')

    def test_comments_escaped_percent_and_verbatim_are_literal(self):
        text = '% \\input{missing}\n\\% \\input{real}\n\\verb|\\input{absent}|\n\\begin{verbatim}\n\\include{absent}\n\\end{verbatim}'
        root = self.put('main.tex', text)
        self.put('real.tex', 'R')
        self.assertEqual(read_tex(root), text.replace('\\input{real}', 'R'))

    def test_dynamic_input_is_not_executed(self):
        root = self.put('main.tex', r'\input{#1}\input{\name}')
        self.assertEqual(read_tex(root), root.read_text())

    def test_missing_reports_source_line_and_chain(self):
        root = self.put('main.tex', '\\input{part}')
        self.put('part.tex', 'one\n\\input{absent}')
        with self.assertRaises(MissingTexSourceError) as caught:
            read_tex(root)
        message = str(caught.exception)
        self.assertIn('part.tex:2', message)
        self.assertIn(str(root), message)
        self.assertIn('absent', message)

    def test_cycle_reports_complete_chain(self):
        root = self.put('main.tex', r'\input{part}')
        part = self.put('part.tex', r'\include{main}')
        with self.assertRaises(TexIncludeCycleError) as caught:
            read_tex(root)
        self.assertIn(f'{root} -> {part} -> {root}', str(caught.exception))

    def test_utf8_bytes_crlf_and_source_spans(self):
        root = self.put('main.tex', 'ä\r\n\\input{part}x\r\n')
        part = self.put('part.tex', 'β\n')
        self.assertEqual(read_tex(root), 'ä\r\nβ\nx\r\n')
        chunks = source_chunks(root)
        for chunk in chunks:
            self.assertEqual(chunk.path.read_bytes()[chunk.start_byte:chunk.end_byte].decode('utf-8'), chunk.text)
        self.assertEqual(chunks[0].start_line, 1)
        self.assertEqual(chunks[0].end_line, 1)
        self.assertEqual(chunks[1].include_chain, (root, part))
        self.assertEqual(chunks[2].start_line, 2)

    def test_compile_directory_precedes_module_directory(self):
        root = self.put('entry.tex', r'\input{modules/main}')
        self.put('modules/main.tex', r'\input{common}')
        self.put('common.tex', 'compile-directory')
        self.put('modules/common.tex', 'module-directory')
        self.assertEqual(read_tex(root), 'compile-directory')

    def test_nested_local_fallback_and_unbraced_input(self):
        root = self.put('entry.tex', '\\input modules/main.tex\n')
        self.put('modules/main.tex', r'\input{local}')
        self.put('modules/local.tex', 'local')
        self.assertEqual(read_tex(root), 'local\n')

    def test_repeated_dependency_is_not_a_cycle(self):
        root = self.put('main.tex', r'\input{part}\input{part}')
        self.put('part.tex', 'P')
        self.assertEqual(read_tex(root), 'PP')

    def test_dependency_paths_include_empty_files_and_pure_wrappers(self):
        root = self.put('main.tex', r'\input{wrapper}')
        wrapper = self.put('wrapper.tex', r'\input{empty}\input{part}')
        empty = self.put('empty.tex', '')
        part = self.put('part.tex', 'P')
        self.assertEqual(dependency_paths(root), [root, wrapper, empty, part])
        self.assertEqual(read_tex(root), 'P')

    def test_declared_verbatim_environment_remains_literal(self):
        text = r'\DefineVerbatimEnvironment{MyVerbatim}{Verbatim}{}' + '\n' + r'\begin{MyVerbatim}\input{absent}\end{MyVerbatim}'
        root = self.put('main.tex', text)
        self.assertEqual(read_tex(root), text)

    def test_optional_version_cache_guard_is_presence_independent(self):
        text = r'\InputIfFileExists{tex-artefacts/version-auto.tex}{}{}'
        root = self.put('main.tex', text)
        self.assertEqual(read_tex(root), text)
        self.assertEqual(dependency_paths(root), [root])
        self.put('tex-artefacts/version-auto.tex', r'\def\TFPTrev{runtime}')
        self.assertEqual(read_tex(root), text)
        self.assertEqual(dependency_paths(root), [root])

    def test_verbatim_declaration_in_preamble_applies_to_body_module(self):
        root = self.put('main.tex', r'\input{preamble}\input{body}')
        preamble = r'\DefineVerbatimEnvironment{MyVerbatim}{Verbatim}{}'
        body = r'\begin{MyVerbatim}\input{absent}\end{MyVerbatim}'
        self.put('preamble.tex', preamble)
        self.put('body.tex', body)
        self.assertEqual(read_tex(root), preamble + body)

    def test_modularizer_keeps_nested_false_conditional_in_one_module(self):
        import importlib.util
        script = Path(__file__).resolve().parents[1] / 'documents/modularize_sources.py'
        spec = importlib.util.spec_from_file_location('tex_modularizer_test', script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        text = r'\documentclass{article}' + '\n' + r'\begin{document}' + '\n'
        text += r'\newif\ifcustom' + '\n' + r'\customfalse' + '\n' + r'\ifcustom' + '\n'
        text += ('Paragraph inside a skipped branch.\n\n' * 300)
        text += r'\ifcase0 nested\else other\fi' + '\n' + r'\fi' + '\n'
        text += r'\section{Visible}' + '\n' + ('Visible paragraph.\n\n' * 200) + r'\end{document}'
        depths = module.conditional_depths(text)
        self.assertEqual(depths[3], 0)  # newif declares, it does not open a branch
        self.assertEqual(depths[-1], 0)
        lines, ranges = module.partitions(text)
        self.assertTrue(any(end-start > 480 for start,end,role in ranges))
        self.assertTrue(all(depths[start] == 0 for start,end,role in ranges))
        self.assertEqual(''.join(''.join(lines[a:b]) for a,b,role in ranges), text)

    def test_modularizer_keeps_dual_mode_header_conditional_whole(self):
        import importlib.util
        script = Path(__file__).resolve().parents[1] / 'documents/modularize_sources.py'
        spec = importlib.util.spec_from_file_location('tex_modularizer_header_test', script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        text = r'\ifdefined\Imported\else' + '\n' + r'\documentclass{article}' + '\n' + r'\begin{document}' + '\n' + r'\fi' + '\n\n' + ('Paragraph.\n\n' * 300)
        lines, ranges = module.partitions(text)
        depths = module.conditional_depths(text)
        self.assertTrue(all(depths[start] == 0 for start,end,role in ranges))
        self.assertEqual(''.join(''.join(lines[a:b]) for a,b,role in ranges), text)


if __name__ == '__main__':
    unittest.main()
