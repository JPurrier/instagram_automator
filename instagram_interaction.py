from instapy_cli import client
import key

class Insta(object):

    def __init__(self):
        pass

    def login_test(self,username=key.username,password=key.password):
        with client(username, password) as cli:
            ig = cli.api()
            print(ig.current_user())

    def post_image(self,image,caption,username=key.username,password=key.password):
        pass