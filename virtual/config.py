import os
class confi:

  NEWS_API_BASE_URL ='http://api.thenewsdb.org/4/news/{}?api_key={}'
  NEWS_API_KEY = os.environ.get('SECRET_KEY')
  SECRET_KEY = os.environ.get('SECRET_KEY') 

class prodConfig(config):  
    pass
    
    class DevConfig(config):
        DEBUG = True

    config_options = {
        'development':DevConfig,
        'production':prodConfig,
    }    