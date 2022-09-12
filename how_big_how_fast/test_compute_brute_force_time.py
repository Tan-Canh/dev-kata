from unittest import TestCase

from src.how_fast import HowFast


class TestComputeBruteForceTime(TestCase):
    def test_it_should_raise_exception_when_input_less_than_0(self):
        self.assertRaises(ValueError, HowFast().compute_brute_force_time, -5)

    def test_it_should_raise_exception_when_input_equal_0(self):
        self.assertRaises(ValueError, HowFast().compute_brute_force_time, 0)

    def test_it_should_return_true_result_when_valid_input(self):
        result = HowFast().compute_brute_force_time(2)
        assert result == 79228162514264337593543950336
