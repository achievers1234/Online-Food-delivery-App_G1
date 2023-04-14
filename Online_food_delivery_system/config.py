import os 

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

@staticmethod
def init_app(app):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    JWT_SECRET_KEY = "super"

    SWAGGER={
        'title':'Online food delivery system',
        'uiversion':3 
    }



    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost/online_food_delivery_system'

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') 

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}  