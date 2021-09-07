class User():
    '''
        Class that models a User

        Fields:
            _server: holds the server's instance
            _ticks: holds the amount of ticks necessary to complete a task

        Methods:
            decrement(): decrements one number from _ticks
            return_server(): returns the server's ID
            return_ticks(): returns the remaning ticks
    '''
    def __init__(self, server, ttask):
        self._server = server
        self._ticks = ttask

    def decrement(self):
        self._ticks -= 1

    def return_server(self):
        return self._server

    def return_ticks(self):
        return self._ticks

class Server():
    """
        Class that models a Server

        Fields:
            _users: keeps the amount of users online
            _id: keeps the server id
            _umax: keeps the server's capacity

        Methods:
            get_users(): returns the number of users curently on the server
            is_available(): returns True or False if there is space in the server
            add_user(): adds a new user to the server
            decrement(): removes a user from the server
    """
    def __init__(self, counter ,umax):
        self._users = 1
        self._id = counter
        self._umax = umax

    def get_users(self):
        return self._users

    def is_available(self):
        if self._users < self._umax:
            return True
        return False

    def add_user(self):
        self._users += 1

    def decrement(self):
        self._users -= 1
