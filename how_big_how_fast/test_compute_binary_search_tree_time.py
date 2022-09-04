from unittest import TestCase, mock

from src.how_big import HowBig
from src.how_fast import HowFast


class TestComputeBinarySearchTreeTime(TestCase):
    @mock.patch.object(HowBig, "get_binary_level_by_number_of_node", return_value=25)
    def test_it_should_raise_exception_when_input_less_than_0(self, mocker):
        mocker.assert_not_called()
        self.assertRaises(ValueError, HowFast().compute_binary_search_tree_time, -5)

    @mock.patch.object(HowBig, "get_binary_level_by_number_of_node", return_value=25)
    def test_it_should_raise_exception_when_input_equal_0(self, mocker):
        mocker.assert_not_called()
        self.assertRaises(ValueError, HowFast().compute_binary_search_tree_time, 0)

    @mock.patch.object(HowBig, "get_binary_level_by_number_of_node", return_value=25)
    def test_it_should_return_true_result_when_valid_input(self, mocker):
        result = HowFast().compute_binary_search_tree_time(10000000)
        mocker.assert_called_once()
        assert result == float(8.16)
