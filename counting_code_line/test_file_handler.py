from unittest import TestCase, mock

from src.file_handler import FileHandler

fake_java_file_name = "test.java"
fake_java_data = """
// comment single-line
/* comment block but single-line */
/*
    
comment multi-line
*/

 
    
int a = 0
/*123*//*123*/
/*123*/123/*123*/
/*123*/123
123/*123*/123
123/*123*/
123//123

/*
*//*
*/

/**/123/*
123
*/123
"""


class TestFileHandler(TestCase):
    def test_it_should_success_to_read_data_from_java_file(self):
        open_mock = mock.mock_open(read_data=fake_java_data)
        with mock.patch("builtins.open", open_mock):
            result = FileHandler().read_java_file(fake_java_file_name)
            assert result == [x for x in fake_java_data.splitlines()]
        open_mock.assert_called_with(
            f"counting_code_line\\data\\{fake_java_file_name}", "r"
        )

    def test_it_should_success_to_read_data_from_empty_dat_file(self):
        open_mock = mock.mock_open(read_data="")
        with mock.patch("builtins.open", open_mock):
            result = FileHandler().read_java_file(fake_java_file_name)
            assert result == []
        open_mock.assert_called_with(
            f"counting_code_line\\data\\{fake_java_file_name}", "r"
        )

    def test_it_should_raise_error_when_read_data_from_file_extension_not_dat(self):
        open_mock = mock.mock_open(read_data="")
        with mock.patch("builtins.open", open_mock):
            self.assertRaises(
                ValueError, FileHandler().read_java_file, "fake_wrong_file_name.xyz"
            )
        open_mock.assert_not_called()
