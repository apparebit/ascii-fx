#!/usr/bin/env python
import contextlib
import io
import unittest

from asciifx.__main__ import main

class TestMain(unittest.TestCase):
    main_args = [
        ['--help'],
    ]
    def test_main_help(self):
        for argv in self.main_args:
            with self.subTest(argv=argv):
                _stderr = io.StringIO()
                _stdout = io.StringIO()
                with contextlib.redirect_stderr(_stderr):
                    with contextlib.redirect_stdout(_stdout):
                        with self.assertRaises(SystemExit) as exc:
                            _ = main(argv=argv)
                        stdout = _stdout.getvalue()
                        stderr = _stderr.getvalue()
                        assert '--help' in stdout, (stdout, stderr) 
                        assert not stderr, (stderr)
                        assert exc.exception.code == 0, (exc.exception.code)


import pytest

@pytest.mark.parametrize('argv', TestMain.main_args)
def test_main_help(argv, capsys):
    with pytest.raises(SystemExit) as exc:
        _ = main(argv=['asciifx', *argv])
    captured = capsys.readouterr()
    assert exc.value.code == 0
    assert '--help' in captured.out, captured
    assert not captured.err, captured