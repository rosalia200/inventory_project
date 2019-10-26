class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:sevani@127.0.0.1:5432/inventory'## dbtype://user:password@host:port/dab_name
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY = 'some secret'



class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://sdoordsqoodqdj:c3b750b4cbc883970b17dbf365ff7c39b555a63e4f1dc6ecd2ea4827d630d1f3@ec2-54-221-215-228.compute-1.amazonaws.com:5432/dad41oigdlr0lb'
    DEBUG = False
    environment ='production'