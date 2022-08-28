from unittest import TestCase, mock

from src.file_handler import FileHandler

fake_dat_file_name = "weather.dat"
fake_dat_data = """
  Dy MxT   MnT   AvT   HDDay  AvDP 1HrP TPcpn WxType PDir AvSp Dir MxS SkyC MxR MnR AvSLP

   1  88    59    74          53.8       0.00 F       280  9.6 270  17  1.6  93 23 1004.5
   2  79    63    71          46.5       0.00         330  8.7 340  23  3.3  70 28 1004.5
"""

fake_csv_file_name = "weather.csv"
fake_csv_data_writer = [
    "Dy MxT   MnT   AvT   HDDay  AvDP 1HrP TPcpn WxType PDir AvSp Dir MxS SkyC MxR MnR AvSLP".split(),
    "1  88    59    74          53.8       0.00 F       280  9.6 270  17  1.6  93 23 1004.5".split(),
    "2  79    63    71          46.5       0.00         330  8.7 340  23  3.3  70 28 1004.5".split(),
]


class TestFileHandler(TestCase):
    def test_it_should_success_to_read_data_from_dat_file(self):
        open_mock = mock.mock_open(read_data=fake_dat_data)
        with mock.patch("builtins.open", open_mock):
            result = FileHandler().read_data_file(fake_dat_file_name)
            assert result == fake_csv_data_writer
        open_mock.assert_called_with(f"data_munging\\data\\{fake_dat_file_name}", "r")

    def test_it_should_success_to_read_data_from_empty_dat_file(self):
        open_mock = mock.mock_open(read_data="")
        with mock.patch("builtins.open", open_mock):
            result = FileHandler().read_data_file(fake_dat_file_name)
            assert result == []
        open_mock.assert_called_with(f"data_munging\\data\\{fake_dat_file_name}", "r")

    def test_it_should_raise_error_when_read_data_from_file_extension_not_dat(self):
        open_mock = mock.mock_open(read_data="")
        with mock.patch("builtins.open", open_mock):
            self.assertRaises(
                ValueError, FileHandler().read_data_file, "fake_wrong_file_name.xyz"
            )
        open_mock.assert_not_called()

    def test_it_should_success_to_write_data_to_csv_file(self):
        open_mock = mock.mock_open()
        with mock.patch("builtins.open", open_mock, create=True):
            FileHandler().write_data_to_csv(fake_csv_data_writer, fake_csv_file_name)
        open_mock.assert_called_with(f"data_munging\\data\\{fake_csv_file_name}", "w+")

    def test_it_should_success_to_write_empty_data_to_csv_file(self):
        open_mock = mock.mock_open()
        with mock.patch("builtins.open", open_mock, create=True):
            FileHandler().write_data_to_csv([], fake_csv_file_name)
        open_mock.assert_called_with(f"data_munging\\data\\{fake_csv_file_name}", "w+")

    def test_it_should_raise_error_when_write_data_to_file_extension_not_csv(self):
        open_mock = mock.mock_open(read_data="")
        with mock.patch("builtins.open", open_mock):
            self.assertRaises(
                ValueError,
                FileHandler().write_data_to_csv,
                [],
                "fake_wrong_file_name.xyz",
            )
        open_mock.assert_not_called()

    def test_it_should_success_to_read_data_from_csv_file(self):
        open_mock = mock.mock_open()
        with mock.patch("builtins.open", open_mock):
            FileHandler().read_csv_file(fake_csv_file_name)
        open_mock.assert_called_with(f"data_munging\\data\\{fake_csv_file_name}", "r")

    def test_it_should_failed_to_read_data_from_file_extension_not_csv(self):
        open_mock = mock.mock_open()
        with mock.patch("builtins.open", open_mock):
            self.assertRaises(
                ValueError, FileHandler().read_csv_file, "fake_wrong_file_name.xyz"
            )
        open_mock.assert_not_called()
