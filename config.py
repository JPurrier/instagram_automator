import json
import os

class ConfigurationSetup(object):
    def __init__(self):
        self.root_path =  os.getenv('APPDATA') + '\\jtools'
        self.content_config_file = r'\content.json'

    def generate_storage_json(self,content_folder, root_path=None):
        root_path = self.root_path if root_path is None else root_path
        config = {
            'root_path'         : root_path,
            'content_folder'    : content_folder
        }
        
        if not os.path.exists(root_path):
            os.makedirs(root_path)
            print('making path '+ root_path)
        with open(root_path + r'\storage.json', 'w') as outfile:
            json.dump(config, outfile)

    def return_storage_config(self):
        if os.path.exists(self.root_path + r'\storage.json'):
            with open(self.root_path + r'\storage.json') as storage_config:
                return json.load(storage_config)
        else:
            raise Exception('Config_Not_Found')

    def create_content_config(self, content_folder):
        config = {}
        if not os.path.exists(self.root_path + self.content_config_file):
            with open(self.root_path + self.content_config_file) as content_config:
                json.dump(config, content_config)
    
    def udpate_content_config(self,id=None,description=None,uid=None,post_date=None,post_time=None,story=None,post=None):
        pass
