
class Credentials:
    '''
    class for generating and managing a user's passwords
    '''
    locker = {}
    def __init__(self, platform, username, password):
        self.platform = platform
        self.username = username
        self.password = password
    def save_cred(self):
        Credentials.locker[self.platform] = {self.username: self.password} # nested dictionary
        print(Credentials.locker)
        print(len(Credentials.locker))
