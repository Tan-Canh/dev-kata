import unittest

from sorting_it_out.__main__ import sorting_it_out


class TestSortingItOut(unittest.TestCase):
    def test_it_should_return_empty_when_input_is_empty(self):
        value = ""
        actual = sorting_it_out(value)
        expect = ""
        self.assertEqual(expect, actual)

    def test_it_should_return_alphabet_only_characters(self):
        value = "<,?':.abcABa"
        actual = sorting_it_out(value)
        expect = "aaabbc"
        self.assertEqual(expect, actual)

    def test_it_should_not_return_any_white_space(self):
        value = " abcAAA"
        actual = sorting_it_out(value)
        expect = "aaaabc"
        self.assertEqual(expect, actual)

    def test_it_should_return_correct_result_when_case_sensitive(self):
        value = "ABCabc"
        actual = sorting_it_out(value, case_sensitive=True)
        expect = "abcABC"
        self.assertEqual(expect, actual)

    def test_it_should_return_correct_result(self):
        value = (
            "When not studying nuclear physics, Bambi likes to play beach volleyball."
        )

        actual = sorting_it_out(value)
        expect = "aaaaabbbbcccdeeeeeghhhiiiiklllllllmnnnnooopprsssstttuuvwyyyy"

        self.assertEqual(expect, actual)
