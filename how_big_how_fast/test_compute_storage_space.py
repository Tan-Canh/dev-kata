from unittest import TestCase

from src.how_big import HowBig


class TestComputeStorageSpace(TestCase):
    def test_it_should_raise_exception_when_input_less_than_0(self):
        self.assertRaises(ValueError, HowBig().compute_storage_space, -1)

    def test_it_should_return_true_size_with_1_standard_record(self):
        result = HowBig().compute_storage_space(1)
        assert result == 315

    def test_it_should_return_0_if_not_any_record(self):
        result = HowBig().compute_storage_space(0)
        assert result == 0
