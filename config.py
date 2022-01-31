import OS
#This module will allow application to interact with operating system
class confi:
    """
    config class  will contain all data that will be usedin development of our project
    """
    NEWS_API_KEY = os.enviroment.get('NEWS_API_KEY')
    SOURCES_BASE_API_URL ="http://newsapi.org/v2/sources?apikey={}"
    EVERYTHING_BASE_API_URL = "http://newsapi.org/v2/everything?domains=wsj.com&apikey={}"
    TOP_HEADLINES_BASE_API_URL = "http://newsapi.org/v2/headlines?sources={}&apikey={}"
    FOOTBALL_TOP_HEADLINES = "http://newsapi.org/v2/football_headlines?country=us&category=football&apikey={}"
