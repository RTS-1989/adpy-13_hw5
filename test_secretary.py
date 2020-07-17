import os
import unittest
import app
import json
from unittest.mock import patch

class Secretary_Test(unittest.TestCase):

    def setUp(self):

        self.directories, self.documents = app.update_date()

        with patch('app.update_date', return_value=(self.directories, self.documents)):
            with patch('app.input', return_value='q'):
                app.secretary_program_start()

    def test_get_doc_owner_name(self):

        with patch('app.input', return_value='11-2'):
            self.assertEqual('Геннадий Покемонов', app.get_doc_owner_name())

    def test_get_all_doc_owners_names(self):
        self.assertEqual(set(item['name'] for item in app.documents), app.get_all_doc_owners_names())

    def test_add_new_doc(self):

        self.assertNotIn('123', app.directories['3'])        
        with patch('app.input', side_effect=['123', 'pasp', 'Igor', '3']):
            app.add_new_doc()            
        self.assertIn('123', app.directories['3'])

    def test_remove_doc_from_shelf(self):
        
        self.assertIn('10006', app.directories['2'])        
        with patch('app.input', return_value='10006'):
            app.remove_doc_from_shelf('10006')           
        self.assertNotIn('10006', app.directories['2'])

    def test_add_new_shelf(self):

        self.assertNotIn('4', app.directories)
        with patch('app.input', return_value='4'):
            app.add_new_shelf('4')
        self.assertIn('4', app.directories)

    def test_append_doc_to_shelf(self):

        self.assertNotIn('123', app.directories)       
        app.append_doc_to_shelf('123', '2')            
        self.assertIn('123', app.directories['2'])

    def test_delete_doc(self):

        self.assertIn('10006', app.directories['2'])
        self.assertIn('10006', app.documents[-1]['number'])       
        with patch('app.input', return_value='10006'):
            app.delete_doc()            
        self.assertNotIn('10006', app.directories['2'])
        self.assertNotIn('10006', app.documents[-1]['number'])

    def test_get_doc_shelf(self):

        with patch('app.input', return_value='11-2'):
            self.assertEqual('1', app.get_doc_shelf())

    def test_move_doc_to_shelf(self):

        self.assertIn('11-2', app.directories['1'])
        self.assertNotIn('11-2', app.directories['2'])
        
        with patch('app.input', side_effect=['11-2', '2']):
            app.move_doc_to_shelf()

        self.assertNotIn('11-2', app.directories['1'])
        self.assertIn('11-2', app.directories['2'])

if __name__ == '__main__':
    unittest.main()
