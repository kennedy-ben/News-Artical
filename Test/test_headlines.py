import unittest
import headlines
Headlines = headlines.Headlines

class TestHeadlines(unittest.TestCase):
    """
    TestHeadlines sub-class defines test cases
    for the Headlines class behaviours.
    Args:
        unittest.TestCase: TestCase class helps in creating test cases.
    """
    
    def setUp(self):
        """
        Set up method to create a news_headlines instance
        before each test cases.
        """        
        self.news_headlines = Headlines("John F.L", "Deep African White Gold", "Ugali, African Prestige meal. Staple food in countries such as Kenya....", "https://beyondthegrid.africa/wp-content/uploads/hero-xs-power-africa-copy.jpg", "https://upload.wikimedia.org/wikipedia/commons/4/48/Ugali_%26_Sukuma_Wiki.jpg", "2000-19-03")


    def tearDown(self):
        self.news_headlines = None

    def test_instance(self):
        """
        This method will only assert if self.news_headlines is an instance of
        Headlines class.
        """
        self.assertTrue(isinstance(self.news_headlines, Headlines)) 

    def test_init_author(self):
        """
        This test case tests if self.news_headlines.author is initialized
        properly.
        """
        self.assertEqual(self.news_headlines.author, "John F.L")

    def test_init_title(self):
        """
        This test case tests if self.news_headlines.title is initialized
        properly.
        """
        self.assertEqual(self.news_headlines.title, "Deep African White Gold")

    def test_init_description(self):
        """
        This test case tests if self.news_headlines.description is initialized
        properly.
        """
        self.assertEqual(self.news_headlines.description, "Ugali, African Prestige meal. Staple food in countries such as Kenya....")

    def test_init_url(self):
        """
        This test case tests if self.news_headlines.url is initialized
        properly.
        """
        self.assertEqual(self.news_headlines.url, "https://beyondthegrid.africa/wp-content/uploads/hero-xs-power-africa-copy.jpg")

    def test_init_urlToImage(self):
        """
        This test case tests if self.news_headlines.urlToImage is initialized
        properly.
        """
        self.assertEqual(self.news_headlines.urlToImage, "https://upload.wikimedia.org/wikipedia/commons/4/48/Ugali_%26_Sukuma_Wiki.jpg")

    def test_init_publishedAt(self):
        """
        This test case tests if self.news_headlines.publishedAt is initialized
        properly.
        """
        self.assertEqual(self.news_headlines.publishedAt, "2022-1-5")


if __name__ == "__main__":
    unittest.main()