from unittest import TestCase

from src.how_big import HowBig


class TestComputeBinaryTreeLevel(TestCase):
    def test_it_should_raise_exception_when_input_less_than_0(self):
        self.assertRaises(ValueError, HowBig().get_binary_level_by_number_of_node, -1)

    def test_it_should_return_0_when_input_equal_0(self):
        result = HowBig().get_binary_level_by_number_of_node(0)
        assert result == 0

    def test_it_should_return_4_when_input_equal_8(self):
        result = HowBig().get_binary_level_by_number_of_node(8)
        assert result == 4
