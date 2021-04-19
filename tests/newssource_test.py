import unittest
from app.models import Newssource
Newssource=news_source.Newssource

class newstest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Newssource class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_newssource=Newssource('id','name','description','www.abcnews.go.com','category','language','country')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_newssource,Newssource))

    def test_init(self):
        """
          test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_newssource.id,'id')
        self.assertEqual(self.new_newssource.name,'name')
        self.assertEqual(self.new_newssource.description,'description')
        self.assertEqual(self.new_newssource.url,'www.abcnews.go.com')
        self.assertEqual(self.new_newssource.category,'category')
        self.assertEqual(self.new_newssource.language,'language')
        self.assertEqual(self.new_newssource.country,'country')
        

