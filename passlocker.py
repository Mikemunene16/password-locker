


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

    @classmethod
    def display_user(cls):
        return cls.user_list


    def delete_user(self):
        """
        A method that deletes a saved account from the user list
        """

        User.user_list.remove(self)    



class Credentials():
    """
    Create Credentials class to generate and verify user credentials.
    """

    credentials_list = []

    @classmethod
    def verify_user(cls, username, password):
        """
        A method to verify whether the user is in the User list or not.
        """

        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                a_user == user.username

        return a_user


    def __init__(self,account,userName, password):
        """
        method that defines user credentials to be stored.
        """

        self.account = account
        self.userName = userName
        self.password = password
        
           





