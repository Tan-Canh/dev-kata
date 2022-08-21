from unittest import TestCase, mock

from src.weather import Weather

fake_data = [
    {"Dy": "1", "MxT": "10", "MnT": "2"},
    {"Dy": "2", "MxT": "9", "MnT": "2"},
    {"Dy": "3", "MxT": "8", "MnT": "2*"},
    {"Dy": "4", "MxT": "7", "MnT": "2"},
    {"Dy": "5", "MxT": "6*", "MnT": "2"},
    {"Dy": "mo", "MxT": "6", "MnT": "2"},
]


class TestWeather(TestCase):
    @mock.patch.object(Weather, "_Weather__get_data", return_value=fake_data)
    def test_it_should_success_when_data_exist(self, mocker):
        result = Weather().get_the_smallest_temperature_spread_day()
        mocker.assert_called_once()
        assert result == {"day": 5, "spread": 4}

    @mock.patch.object(Weather, "_Weather__get_data", return_value=[])
    def test_it_should_raise_error_when_data_not_exist(self, mocker):
        self.assertRaises(ValueError, Weather().get_the_smallest_temperature_spread_day)
        mocker.assert_called_once()
