from unittest import TestCase, mock

from src.soccer import Soccer

fake_data = [
    {
        "Team": "1.",
        "P": "Arsenal",
        "W": "38",
        "L": "26",
        "D": "9",
        "F": "3",
        "A": "79",
        "Pts": "-",
        None: ["36", "78"],
    },
    {
        "Team": "1.",
        "P": "Liverpool",
        "W": "38",
        "L": "26",
        "D": "9",
        "F": "3",
        "A": "33",
        "Pts": "-",
        None: ["79", "78"],
    },
    {
        "Team": "--------------------------------------",
        "P": None,
        "W": None,
        "L": None,
        "D": None,
        "F": None,
        "A": None,
        "Pts": None,
        None: None,
    },
]


class TestSoccer(TestCase):
    @mock.patch.object(Soccer, "_Soccer__get_data", return_value=fake_data)
    def test_it_should_success_when_data_exist(self, mocker):
        result = Soccer().get_the_smallest_goal_difference_team()
        mocker.assert_called_once()
        assert result == {"team": "Liverpool", "difference": -46}

    @mock.patch.object(Soccer, "_Soccer__get_data", return_value=[])
    def test_it_should_raise_error_when_data_not_exist(self, mocker):
        self.assertRaises(ValueError, Soccer().get_the_smallest_goal_difference_team)
        mocker.assert_called_once()
