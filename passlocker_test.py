import unittest
from passlocker import User


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

if __name__ == '__main__':
    unittest.main()        


