import unittest
import cap

class TestCap(unittest.TestCase): # inherit
    
    def test_one_word(self):
        text = 'python' # arrange
        result = cap.cap_text(text) # act
        self.assertEqual(result, 'Python') # assert
        
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')
        
    def test_with_apostrophes(self):
        text = "monty python's flying circus"
        result = cap.cap_text(text)
        self.assertEqual(result, "Monty Python's Flying Circus")
        
if __name__ == '__main__':
    unittest.main() # call main