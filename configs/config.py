class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:sevani@127.0.0.1:5432/inventory'## dbtype://user:password@host:port/dab_name
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY = 'some secret'



class Development(Config):
    pass