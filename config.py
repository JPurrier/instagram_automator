import json
import os
import hashlib
from database import DatabaseInteractions
import tables

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

    def create_content_entry(self,conn,item):

        sql = ''' INSERT INTO content(file_name,description,post_date,story)
                      VALUES(?,?,?,?); '''
        cur = conn.cursor()
        cur.execute(sql, item)
        conn.commit()
        return cur.lastrowid

    def get_content_info(self):
        storage_config = ConfigurationSetup().return_storage_config()
        db_connection = DatabaseInteractions().create_connection(
            (storage_config['root_path'] + '\\' + self.database_name))

        c = db_connection.cursor()
        # Get table contents
        c.execute('SELECT * FROM content')
        sql_content_table = c.fetchall()
        return sql_content_table



    def update_content_info(self,jid=None,file_name=None,description=None,
                                post_date=None,story=None,reindex=None):
        storage_config = ConfigurationSetup().return_storage_config()
        db_connection = DatabaseInteractions().create_connection((storage_config['root_path'] + '\\' + self.database_name))

        list_of_content = os.listdir(storage_config['content_folder'])
        # Get Content table from DB if table is missing initialise table
        c = db_connection.cursor()
            # Creates table if ! exist
        c.execute(tables.content_table)
        # Get Current Database Config


        # if no options are called scan directory and create entry for each item
        if(jid is None and description is None and post_date is None
            and story is None and file_name is None and reindex is None):
            print('No option selected running scan and update')
            # Check each item in directory to see if its in the database

                # if in database continue

                # if not in database check for jid

                # if no jid add to database and write metadata jid
            pass


         

        # if content_item is specified will create entry for specfic entry
        # if any other option is specified it will update the option id or uid will be manditory
        db_connection.close()

if __name__ == '__main__':
    ConfigurationSetup().update_content_config()


