import os


class Config:
    '''
    General parent class for configuration
    '''
    
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