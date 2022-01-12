import unittest
import requests
class TestCase(unittest.TestCase):
    def setUp(self):
        print('setUp method execution..')
    def test_method(self):
        print('test method execution..')
        response = requests.get('https://firms.modaps.eosdis.nasa.gov')
        if response.status_code == 200:
            print('Web site exists')
        else:
            print('Web site does not exist') 
    def tearDown(self):
        print('tearDown method execution..')

unittest.main()