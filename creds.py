
class Credentials:
    '''
    class for generating and managing a user's passwords
    '''
    def __init__(self, platform, username, password):
        self.platform = platform
        self.username = username
        self.password = password
