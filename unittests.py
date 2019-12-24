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
        c = con.cursor()
        c.execute("select exists(select 1 from content where file_name='file_testx');")
        result_bool = c.fetchall()
        con.close()
        print(result_bool)
        bool_result = True if 1 in result_bool else False
        print(bool_result)
        #self.assertTrue(bool_result[0])

        # check if record exists

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