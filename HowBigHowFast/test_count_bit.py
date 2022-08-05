from unittest import TestCase

from src.how_big import HowBig


class TestCountBit(TestCase):
    def test_it_should_return_1_when_input_equal_0(self):
        result = HowBig().count_bit(0)
        assert result == 1

    def test_it_should_return_1_when_input_equal_1(self):
        result = HowBig().count_bit(1)
        assert result == 1

    def test_it_should_raise_exception_when_input_less_than_0(self):
        self.assertRaises(ValueError, HowBig().count_bit, -1000)

    def test_it_should_return_10_when_input_equal_1000(self):
        result = HowBig().count_bit(1000)
