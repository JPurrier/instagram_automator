import json
import os


class ConfigurationSetup(object):
    def __init__(self):
        self.root_path =  "C:\\Program Files\\jtools\\insta_automator"


    def generate_storage_json(self,root_path, content_folder):
        root_path = self.root_path if root_path is None else root_path
        config = {
            'root_path'         : root_path,
            'content_folder'    : content_folder
        }
        data = {}
        with open(self.root_path + '\\storage.json', 'w') as outfile:
            json.dump(data, outfile)

    def return_storage_config(self):
        if os.path.exists("self.root_path + '\\storage.json'"):
            with open(self.root_path + '\\storage.json') as storage_config:
                pass
        else:
            raise Exception('File_Not_Found')
