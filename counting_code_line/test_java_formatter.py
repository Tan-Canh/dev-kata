from copy import copy
from unittest import TestCase

from src.java_formatter import JavaFormatter

full_lines = [
    "",
    " ",
    "\t",
    " \t",
    "// comment single-line",
    "/* comment block but single-line */",
    "/*",
    "\t",
    "comment multi-line",
    "*/",
    "/*123*//*123*/",
    "/*123*/123/*123*/",
    "/*123*/123",
    "123/*123*/123",
    "123/*123*/",
    "123//123",
    "/*",
    "*//*",
    "*/",
    "/**/123/*",
    "123",
    "*/123",
    "int a = 0",
]
no_single_comment_lines = [
    "",
    " ",
    "\t",
    " \t",
    "/* comment block but single-line */",
    "/*",
    "\t",
    "comment multi-line",
    "*/",
    "/*123*//*123*/",
    "/*123*/123/*123*/",
    "/*123*/123",
    "123/*123*/123",
    "123/*123*/",
    "123//123",
    "/*",
    "*//*",
    "*/",
    "/**/123/*",
    "123",
    "*/123",
    "int a = 0",
]
no_block_comment_lines = [
    "",
    " ",
    "\t",
    " \t",
    "// comment single-line",
    "",
    "",
    "",
    "",
    "",
    "",
    "123",
    "123",
    "123123",
    "123",
    "123//123",
    "",
    "",
    "",
    "123",
    "",
    "123",
    "int a = 0",
]
no_blank_lines = [
    "// comment single-line",
    "/* comment block but single-line */",
    "/*",
    "comment multi-line",
    "*/",
    "/*123*//*123*/",
    "/*123*/123/*123*/",
    "/*123*/123",
    "123/*123*/123",
    "123/*123*/",
    "123//123",
    "/*",
    "*//*",
    "*/",
    "/**/123/*",
    "123",
    "*/123",
    "int a = 0",
]


class TestJavaFormatter(TestCase):
    def test_single_line_comments_should_be_remove_from_lines(self):
        result = JavaFormatter().remove_single_line_comments(copy(full_lines))
        assert result == no_single_comment_lines

    def test_block_comments_should_be_remove_from_lines(self):
        result = JavaFormatter().remove_block_comments(copy(full_lines))
        assert result == no_block_comment_lines

    def test_blank_lines_should_be_remove_from_line_list(self):
        result = JavaFormatter().remove_blank_lines(copy(full_lines))
        assert result == no_blank_lines

    # TODO: handle case: print("/*")
    # TODO: handle case: print("a") // hello
    # TODO: handle case: print("//")
