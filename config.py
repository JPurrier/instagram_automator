import json
import os
import hashlib
from database import DatabaseInteractions
import tables
import hashlib



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

        sql = ''' INSERT INTO content(file_name,description,post_date,story,posted,jid)
                      VALUES(?,?,?,?,?,?); '''
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

    def get_content_hash(self,content):
        BLOCKSIZE = 65536
        hasher = hashlib.md5()
        with open(content, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        return(hasher.hexdigest())

    def initialise_db_content(self,list_of_content):
        storage_config = ConfigurationSetup().return_storage_config()
        db_connection = DatabaseInteractions().create_connection(
            (storage_config['root_path'] + '\\' + self.database_name))
        c = db_connection.cursor()
        content_update_table = []
        for content in list_of_content:
            jid = ConfigurationSetup().get_content_hash(
                storage_config['content_folder'] + '\\' + content)
            data_to_input_into_db = (content, jid)
            c.execute(tables.add_content, data_to_input_into_db)
            db_connection.commit()
            content_update_table.append({content:jid})
        return content_update_table

    def update_content_info(self,id=None,file_name=None,description=None,
                                post_date=None,story=None,posted=None,jid=None):
        storage_config = ConfigurationSetup().return_storage_config()
        db_connection = DatabaseInteractions().create_connection((storage_config['root_path'] + '\\' + self.database_name))

        list_of_content = os.listdir(storage_config['content_folder'])
        print('LIST OF CONTENT: {}'.format(list_of_content))
        # Get Content table from DB if table is missing initialise table
        c = db_connection.cursor()
            # Creates table if ! exist
        c.execute(tables.content_table)
        db_connection.commit()
        # Get Current Database Config
        db_entries = ConfigurationSetup().get_content_info()

        # if no options are called scan directory and create entry for each item
        if(jid is None and description is None and post_date is None
            and story is None and file_name is None):
            # Check each item in directory to see if its in the database
            if not db_entries:
                # if database is empty
                ConfigurationSetup().initialise_db_content(list_of_content)
                return 'Database Empty initialisation run'

            for content in list_of_content:
                # if in database continue
                i = 0

                for row in db_entries:
                    if content in row:
                        print('in db :' + content)
                        i = 1
                        continue
                    else:
                        jid = ConfigurationSetup().get_content_hash(storage_config['content_folder'] + '\\' + content)
                        # if not in database get hash / jid
                        if jid in row:
                            print('Need to update name in db')
                            #print('hash in db: ' + jid)
                            print('name:' + content)
                            print(row)
                            # update name field with new name
                            update_content = (content,row[0])
                            c.execute(tables.update_name, update_content)
                            db_connection.commit()
                            i = 1

                if i == 1:
                    continue
                else:
                    print('i {} c {}'.format( i, content))
                    if i != 1:
                        # add item to database
                        print('i = {} content = {} '.format(i,  content))
                        data_to_input_into_db = (content, jid)
                        print('Added: {} | {}'.format(content, jid))
                        c.execute(tables.add_content, data_to_input_into_db)
                        db_connection.commit()



        # if content_item is specified will create entry for specfic entry
        # if any other option is specified it will update the option id or uid will be manditory

        db_connection.close()

    def reindex_db(self,reindex=False):
        pass

if __name__ == '__main__':
    ConfigurationSetup().update_content_config()


