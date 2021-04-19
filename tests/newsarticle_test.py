import unittest
from app.Models import news_article
class newsarticletest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Newsarticle class
    """

    def setUp(self):
        """
         Set up method that will run before every Test
        """

        self.new_newsarticle=Newsarticle('author','title','description','www.news.com','urltoimage','2020-04-03T10:09:32Z','content')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_newsarticle,Newsarticle))

    def test_init(self):
        self.assertEqual(self.new_newsarticle.author,'author')
        self.assertEqual(self.new_newsarticle.title,'title')
        self.assertEqual(self.new_newsarticle.description,'description')
        self.assertEqual(self.new_newsarticle.url,'www.news.com')
        self.assertEqual(self.new_newsarticle.urlToImage,'urltoimage')
        self.assertEqual(self.new_newsarticle.publishedAt,'2020-04-03T10:09:32Z')
        self.assertEqual(self.new_newsarticle.content,'content')
