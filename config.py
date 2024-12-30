class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SECRET_KEY = "thisissecret" #whenever you are using the session you have to use secret key flask security build on the top of the flask login
    SECURITY_PASSWORD_SALT = "thisissaltforencryption" #salt is used to encrypt the password
    SQLALCHEMY_TRACK_MODIFICATIONS = False #where you have to track the modification
    WTF_CSRF_ENABLED = False #csrf token means request come from the legitment frontend(whenever you generate a form you add a csrf token and when some user fill that form then csfr token also come if the csrf token mathces the generated token flask will accept the request o/w not )
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token'
    



     
  