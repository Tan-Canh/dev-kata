from unittest import TestCase, mock

from src.file_handler import FileHandler
from src.java_code import JavaCode

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
only_code_lines = [
    "123",
    "123",
    "123123",
    "123",
    "123//123",
    "123",
    "123",
    "int a = 0",
]
fake_java_file_name = "test.java"


class TestJavaCode(TestCase):
    @mock.patch.object(FileHandler, "read_java_file", return_value=full_lines)
    def test_it_should_return_list_of_code_line_only(self, mocker):
        result = JavaCode().get_valid_lines(fake_java_file_name)
        mocker.assert_called_once()
        assert result == only_code_lines

    @mock.patch.object(FileHandler, "read_java_file", return_value=[])
    def test_it_should_return_list_of_code_line_only(self, mocker):
        result = JavaCode().get_valid_lines(fake_java_file_name)
        mocker.assert_called_once()
        assert result == []
