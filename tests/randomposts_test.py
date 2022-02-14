import unittest
from models.randomposts_class import Random

class RandomQuotesTest(unittest.TestCase):
    def setUp(self):
        self.new_quote = Random('1','James Winters','Winter is coming soon!',)
        
    def test_init(self):
        self.assertEqual(self.new_quote.id,'1')       
        self.assertEqual(self.new_quote.author,'James Winters')       
        self.assertEqual(self.new_quote.last_name,'Winter is coming soon!')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Random))


if __name__ == '__main__':
    unittest.main()