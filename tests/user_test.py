import unittest
from models.user_class import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User('1','Ivy','Murithi','Feuer','ivymurithi@gmail.com','1234567895DBJAD')
        
    def test_init(self):
        self.assertEqual(self.new_user.id,'1')       
        self.assertEqual(self.new_user.first_name,'Ivy')       
        self.assertEqual(self.new_user.last_name,'Murithi')
        self.assertEqual(self.new_user.username,'Feuer')
        self.assertEqual(self.new_user.email,'ivymurithi@gmail.com')
        self.assertEqual(self.new_user.password,'1234567895DBJAD')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))


if __name__ == '__main__':
    unittest.main()