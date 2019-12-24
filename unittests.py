import unittest
from config import ConfigurationSetup
from database import DatabaseInteractions

class TestConfig(unittest.TestCase):

    def test_create_db_entry(self):
        storage_config = ConfigurationSetup().return_storage_config()
        con = DatabaseInteractions().create_connection(
            (storage_config['root_path'] + '\\' + ConfigurationSetup().database_name))
        test = ('file_testx', 'th_is a test description', 'hh', 'story')
        ConfigurationSetup().create_content_entry(con, test)
        con.commit()
        con.close()

if __name__ == '__main__':
    unittest.main()

    # Clean up db
    storage_config = ConfigurationSetup().return_storage_config()
    con = DatabaseInteractions().create_connection(
        (storage_config['root_path'] + '\\' + ConfigurationSetup().database_name))
    test = ('file_testx', 'th_is a test description', 'hh', 'story')
    ConfigurationSetup().create_content_entry(con, test)
    con.cursor().execute("delete from content where file_name=(?)", ('file_testx',))
    con.commit()
    con.close()