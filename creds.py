
class Credentials:
    '''
    class for generating and managing a user's passwords
    '''
    locker = {}
    def __init__(self, platform, username, password):
        self.platform = platform
        self.username = username
        self.password = password

    def save_password(self):
        Credentials.locker[self.platform] = {self.username: self.password} # nested dictionary
        print(Credentials.locker)
        print(len(Credentials.locker))

    @classmethod
    def display_password(clas):
        return Credentials.locker # have to print
        
    def delete_password(self):
        del Credentials.locker[self.platform]
        print(len(Credentials.locker))

