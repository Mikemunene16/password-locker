import unittest
from passlocker import User
from passlocker import Credentials


class TestClass(unittest.TestCase):
    """
    A test class that defines test cases for the User class behaviours.
    """
    def setUp(self):
        """
        Method that runs before each individual test method run.
        """
        self.new_user = User("mikey", "654321")

    def test_init(self):
        """
        test case to check if the object has been initialized correctly.
        """

        self.assertEqual(self.new_user.username, "mikey")
        self.assertEqual(self.new_user.password, "654321")


    def test_save_user(self):
        """
        test case to test if new user instance has been saved to the User list
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for class Credentials.
    """

    def setUp(self):
        """
        Method that runs before each individual credentials test method run.
        """

        self.new_credential = Credentials("Instagram", "mikey", "09876")

    def test_init(self):
        """
        Test case to check if new Credentials has been initialized correctly
        """

        self.assertEqual(self.new_credential.account , "Instagram") 
        self.assertEqual(self.new_credential.userName, "mikey") 
        self.assertEqual(self.new_credential.password, "09876")








if __name__ == '__main__':
    unittest.main()        


