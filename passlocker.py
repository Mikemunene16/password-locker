


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

        