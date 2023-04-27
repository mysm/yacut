import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "nmZN2sGM394ntyKMcj014rGPrlJemvRd")
    TEMPLATE_FOLDER = os.path.abspath(os.getenv("TEMPLATE_FOLDER", "html"))
    STATIC_FOLDER = os.path.abspath(os.getenv("STATIC_FOLDER", "html"))
