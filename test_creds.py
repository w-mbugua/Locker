import unittest
from creds import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("Twitter", "JM", "Password2021")

    def test_init(self):
        '''
        test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.platform, "Twitter")
        self.assertEqual(self.new_credential.username, "JM")
        self.assertEqual(self.new_credential.password, "Password2021")

    def test_save_manager(self):
        '''
        test to check whether the password details are saved 
        '''
        self.new_credential.save_cred()
        self.assertEqual(len(Credentials.locker), 1)


    
if __name__ == '__main__':
    unittest.main()
