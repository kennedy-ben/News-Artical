import os

class Config:
    """
    Config class will contain all(general) configurations/optimization
    that will will be used in Development stage and Production class.
    """
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SOURCES_BASE_API_URL = "https://newsapi.org/v2/sources?apiKey={}"
    EVERYTHING_BASE_API_URL = "https://newsapi.org/v2/everything?domains=wsj.com&apikey={}"
    TOP_HEADLINES_BASE_API_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    BUSINESS_TOP_HEADLINES = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={}"


class ProdConfig(Config):
    """    
    This sub-class will also contain all the other configurations to
    facilitate the production class. 
    
    """
    pass


class DevConfig(Config):
    """
    Sub-class contains all configurations that will facilate the development stage.
    
          
    """
  
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig