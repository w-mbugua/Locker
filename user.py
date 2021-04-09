class User:
    '''A class for the password locker account'''
    users = {}
    def __init__(self, name, password):
        self.name = name
        self.password = password
        
    def save_manager(self):
        User.users[self.name] = self.password