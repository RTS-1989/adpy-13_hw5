import unittest
import requests
import translator
import os

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

class Test(unittest.TestCase):

    def test_positive_response(self):
        
        params = {'key': API_KEY,
                  'text': 'response',
                  'lang': '%s''-%s' % ('en', 'ru')
                  }
        response = requests.get(URL, params=params).json()
        self.assertEqual(200, response['code'])

    def test_positive_answer(self):
        
        params = {'key': API_KEY,
                  'text': 'hello',
                  'lang': '%s''-%s' % ('en', 'ru')
                  }
        response = requests.get(URL, params=params).json()
        self.assertEqual('привет', response['text'][0])

    def test_negative_answer(self):
        
        params = {'key': API_KEY,
                  'text': 'dog',
                  'lang': '%s''-%s' % ('en', 'ru')
                  }
        response = requests.get(URL, params=params).json()
        self.assertNotEqual('кот', response['text'][0])

    def test_wrong_api_key(self):
        
        params = {'key': 'Some_wrong_key',
                  'text': 'hello',
                  'lang': '%s''-%s' % ('en', 'ru')
                  }
        response = requests.get(URL, params=params).json()
        self.assertNotEqual(200, response['code'])

    def test_translated_file_exists(self):

        translator.translate_it('ES.txt', 'translated.txt', 'es', 'ru')
        self.assertTrue(os.path.exists('C:\\Homework\\translated.txt'))

if __name__ == '__main__':
    unittest.main()

        
