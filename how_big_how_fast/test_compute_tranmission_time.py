from unittest import TestCase

from src.how_fast import HowFast


class TestComputeTranmissionTime(TestCase):
    def test_it_should_raise_exception_when_input_less_than_0(self):
        self.assertRaises(ValueError, HowFast().compute_tranmission_time, -5, -5, -5)

    def test_it_should_raise_exception_when_input_equal_0(self):
        self.assertRaises(ValueError, HowFast().compute_tranmission_time, 0, 0, 0)

    def test_it_should_return_true_result_when_valid_input(self):
        result = HowFast().compute_tranmission_time(1200, 56000)
        assert result == 857

    def test_it_should_return_true_result_when_change_modem_coeficient(self):
        result = HowFast().compute_tranmission_time(1200, 56000, 5)
        assert result == 171
