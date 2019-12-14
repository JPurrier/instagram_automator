from instapy_cli import client
import key

class Insta (object):
    def __init__(self):
        self.username = key.username
        self.password = key.password
        self.image    = ''
        self.caption  = ''

    def login_test(self,username=self.username,password=self.password):
        with client(username, password) as cli:
            ig = cli.api()
            print(ig.current_user())



