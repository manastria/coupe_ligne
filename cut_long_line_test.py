import unittest

from cut_long_line import cut_long_line


class TestCutLongLine(unittest.TestCase):
    def test_cut_long_line_with_alignment(self):
        long_line = 'result = arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8 + arg9 + arg10'
        cut_line = cut_long_line(long_line, max_length=30, cut_indicator='✂', indent_chars=[' '], align_chars=['=', '+'])
        expected_cut_line = 'result = arg1 + arg2 + arg3 +✂\n         arg4 + arg5 + arg6 + arg7 +✂\n         arg8 + arg9 + arg10'
        self.assertEqual(cut_line, expected_cut_line)

    def test_cut_long_line_without_alignment(self):
        log_line = '2023-04-21 12:34:56 [INFO] This is a very long log line that needs to be cut to fit the page width properly'
        cut_log_line = cut_long_line(log_line, max_length=40, cut_indicator='✂', indent_chars=[' '])
        expected_cut_log_line = '2023-04-21 12:34:56 [INFO] This✂\n  is a very long log line that needs to be cut✂\n  to fit the page width properly'
        self.assertEqual(cut_log_line, expected_cut_log_line)

unittest.main()