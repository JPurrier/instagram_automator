import unittest
from config import ConfigurationSetup
from database import DatabaseInteractions

class TestConfig(unittest.TestCase):

    def test_update_content_info(self):
        print('****Running update_content_config module no options selected')
        result = ConfigurationSetup().update_content_info()
        print(result)

    def test_create_db_entry(self):
        print('****Testing that Record is being created')
        storage_config = ConfigurationSetup().return_storage_config()
        con = DatabaseInteractions().create_connection(
            (storage_config['root_path'] + '\\' + ConfigurationSetup().database_name))
        test = ('file_testx', 'th_is a test description', 'DATE', 'Story_text','TRUE', '4d901fe1411f32455e59b9309d63b6fx')
        ConfigurationSetup().create_content_entry(con, test)
        con.commit()
        c = con.cursor()
        c.execute("select exists(select 1 from content where file_name='file_testx');")
        result_bool = c.fetchall()
        con.close()

        bool_result = True if 1 in result_bool[0] else False
        print(bool_result)
        self.assertTrue(bool_result)

    def test_delete_db_entry(self):
        print('****Testing removing Database Entry(s)')  # Clean up db
        storage_config = ConfigurationSetup().return_storage_config()
        con = DatabaseInteractions().create_connection(
            (storage_config['root_path'] + '\\' + ConfigurationSetup().database_name))
        con.cursor().execute("delete from content where file_name=(?)", ('file_testx',))
        con.commit()
        con.cursor().execute("select exists(select 1 from content where file_name='file_testx');")
        result_bool = con.cursor().fetchall()
        con.close()
        self.assertFalse(result_bool)

    def test_get_content_info(self):
        print('****Check get content method')
        result = ConfigurationSetup().get_content_info()
        print(result)

    def test_return_storage_config(self):
        ConfigurationSetup().return_storage_config()

    def test_get_content_hash(self):
        print('****** Get image hash *****')
        result = ConfigurationSetup().get_content_hash('c:\\sample\\IMG_6183.JPG')
        print('Hash MD5: ' + result)


if __name__ == '__main__':
    import os
    os.system('cls')
    unittest.main()
