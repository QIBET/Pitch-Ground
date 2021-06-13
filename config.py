import os


class Config:
    '''
    General parent class for configuration
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Sotik2020*@localhost/pitchground'
    
class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: General parent class for configuration
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: General parent class for configuration
    '''

    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}