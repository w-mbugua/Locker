
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
        '''
        method for saving passwords and their respective platforms
        '''
        Credentials.locker[self.platform] = {self.username: self.password} # nested dictionary
        print(Credentials.locker)
        print(len(Credentials.locker))

    @classmethod
    def display_password(clas):
        '''
        method to display all passwords saved
        '''
        for item in Credentials.locker:
            print(item.upper(),'.....')
            item = Credentials.locker[item]
            for key in item:
                print(f"Username: {key}; Password: {item[key]}\n")
        
    def delete_password(self):
        '''
        method to display all passwords saved
        '''
        del Credentials.locker[self.platform]
        print(len(Credentials.locker))

