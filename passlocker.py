


class User:
    """
    Create User class that generates new instance of a user.
    """

    user_list = []

    def __init__(self, username, password):
        """
        method that define properties of user.
        """
        self.username = username
        self.password = password


    def save_user(self):
        """
        A method that saves a new user instance in the user list.
        """

        User.user_list.append(self) 
        
           

