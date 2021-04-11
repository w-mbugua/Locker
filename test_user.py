import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Doe", "bRt456")

    def test_init(self):
        '''
        test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.name, "Doe")
        self.assertEqual(self.new_user.password, "bRt456")
    def test_save_manager(self):
        '''
        test to check whether the manager login details are saved 
        '''
        self.new_user.save_manager()
        self.assertEqual(len(User.users), 1)
if __name__ == '__main__':
    unittest.main()