import main    
import unittest   
from sqlalchemy import false

class Test_Sorting_It_Out(unittest.TestCase):
    def test_it_should_return_false_if_there_is_no_ball_to_sort(self):
        drawn_numbers_list = []
        actual_value = main.sorting_balls(drawn_numbers_list)
        expected_list = false
        self.assertEqual(actual_value, expected_list)
        
    def test_it_should_return_sorted_list_if_there_are_values_in_drawn_list(self):
        drawn_numbers_list = [3, 2, 1]
        actual_value = main.sorting_balls(drawn_numbers_list)
        expected_list = [1, 2, 3]
        self.assertEqual(actual_value, expected_list)
        
    def test_it_should_return_sorted_list_if_there_are_more_values_added_to_drawn_list(self):
        drawn_numbers_list = [3, 2, 1]
        drawn_numbers_list.append(50)
        actual_value = main.sorting_balls(drawn_numbers_list)
        expected_list = [1, 2, 3, 50]
        self.assertEqual(actual_value, expected_list)  
        
    def test_it_should_return_sorted_list_if_there_are_more_multilple_values_added_to_drawn_list(self):
        drawn_numbers_list = [10, 20]
        actual_value = main.sorting_balls(drawn_numbers_list)
        self.assertEqual(actual_value, actual_value)   
        drawn_numbers_list.append(20)
        self.assertEqual(actual_value, drawn_numbers_list)
        drawn_numbers_list.append(10)
        self.assertEqual(actual_value, drawn_numbers_list)
        drawn_numbers_list.append(12)
        self.assertEqual(actual_value, drawn_numbers_list)
if __name__ == '__main__':
    unittest.main()