import json
import os
import hashlib
from database import DatabaseInteractions

class ConfigurationSetup(object):
    def __init__(self):
        self.root_path =  os.getenv('APPDATA') + '\\jtools'
        self.content_config_file = r'\content.json'
        self.database_name = 'Jtools_instagram.db'

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

    def update_content_config(self,jid=None,file_name=None,description=None,
                                post_date=None,story=None):
        '''
        if no input should create database
        >>> ConfigurationSetup().update_content_config()
        (2, 6, 0)
        No option selected

        '''
        storage_config = ConfigurationSetup().return_storage_config()
        db_connection = DatabaseInteractions().create_connection((storage_config['root_path'] + '\\' + self.database_name))
        db_connection.close()
        list_of_content = os.listdir(storage_config['content_folder'])
        # Get Content table from DB if table is missing initialise table
        
        # if no options are called scan directory and create entry for each item
        if(jid is None and description is None and post_date is None
            and story is None and file_name is None):
            print('No option selected')
            print(list_of_content)

         

        # if content_item is specified will create entry for specfic entry
        # if any other option is specified it will update the option id or uid will be manditory
        
if __name__ == '__main__':
    ConfigurationSetup().update_content_config()
    import doctest
    #doctest.testmod()