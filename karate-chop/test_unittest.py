import main    
import unittest   

class Test_Chop(unittest.TestCase):
    # Recursive tests
    def test_recursive_binary_search_case_1(self):
        arr = [] 
        self.assertEqual(main.recursive_binary_search(arr, 0, len(arr)-1, 3), -1)
        
    def test_recursive_binary_search_case_2(self):
        arr = [ 1 ] 
        self.assertEqual(main.recursive_binary_search(arr, 0, len(arr)-1, 3), -1)
        
    def test_recursive_binary_search_case_3(self):
        arr = [ 1 ]
        self.assertEqual(main.recursive_binary_search(arr, 0, len(arr)-1, 1), 0)

    def test_recursive_binary_search_case_4(self):
        arr = [1, 3, 5]
        self.assertEqual(main.recursive_binary_search(arr, 0, len(arr)-1, 1), 0)  
        
    def test_recursive_binary_search_case_5(self):
        arr = ['1', '3', '5']
        self.assertEqual(main.recursive_binary_search(arr, 0, len(arr)-1, 1), 0) 
        
    def test_recursive_binary_search_case_6(self):
        arr = ['1', 3, 5]
        self.assertEqual(main.recursive_binary_search(arr, 0, len(arr)-1, 1), 0) 
    
    def test_recursive_binary_search_case_7(self):
        arr = [1, '3', '5']
        self.assertEqual(main.recursive_binary_search(arr, 0, len(arr)-1, 1), 0)
         
    def test_recursive_binary_search_case_8(self):
        arr = ['1', 3, 5]
        self.assertEqual(main.recursive_binary_search(arr, 0, len(arr)-1, '1'), 0) 
        
    def test_recursive_binary_search_case_9(self):
        arr = ['1', '3', '5']
        self.assertEqual(main.recursive_binary_search(arr, 0, len(arr)-1, '1'), 0) 
        
    # Iterative tests
    def test_iterative_binary_search_case_10(self):
        arr = [] 
        self.assertEqual(main.iterative_binary_search(arr, 3), -1)
        
    def test_iterative_binary_search_case_11(self):
        arr = [ 1 ] 
        self.assertEqual(main.iterative_binary_search(arr, 3), -1)
        
    def test_iterative_binary_search_case_12(self):
        arr = [ 1 ]
        self.assertEqual(main.iterative_binary_search(arr, 1), 0)

    def test_iterative_binary_search_case_13(self):
        arr = [1, 3, 5]
        self.assertEqual(main.iterative_binary_search(arr, 1), 0)  
        
    def test_iterative_binary_search_case_14(self):
        arr = ['1', '3', '5']
        self.assertEqual(main.iterative_binary_search(arr, 1), 0) 
        
    def test_iterative_binary_search_case_15(self):
        arr = ['1', 3, 5]
        self.assertEqual(main.iterative_binary_search(arr, 1), 0) 
    
    def test_iterative_binary_search_case_16(self):
        arr = [1, '3', '5']
        self.assertEqual(main.iterative_binary_search(arr, 1), 0)
         
    def test_iterative_binary_search_case_17(self):
        arr = ['1', 3, 5]
        self.assertEqual(main.iterative_binary_search(arr, '1'), 0) 
        
    def test_iterative_binary_search_case_18(self):
        arr = ['1', '3', '5']
        self.assertEqual(main.iterative_binary_search(arr, '1'), 0) 
if __name__ == '__main__':
    unittest.main()