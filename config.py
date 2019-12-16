import json
import os


class ConfigurationSetup(object):
    def __init__(self):
        self.root_path =  r'C:\Program Files\jtools\insta_automator'

    def generate_storage_json(self,content_folder, root_path=None):
        root_path = self.root_path if root_path is None else root_path
        config = {
            'root_path'         : root_path,
            'content_folder'    : content_folder
        }
        data = {}
        if not os.path.exists(root_path):
            
            os.makedirs(root_path)
            print('making path '+ root_path)

        with open(root_path + r'\storage.json', 'w') as outfile:
            json.dump(data, outfile)

    def return_storage_config(self):
        if os.path.exists("self.root_path + r'\storage.json'"):
            with open(self.root_path + r'\storage.json') as storage_config:
                return json.load(storage_config)
        else:
            raise Exception('File_Not_Found')
