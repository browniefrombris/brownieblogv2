import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    RECAPTCHA_PUBLIC_KEY = os.environ.get('6Leux-MiAAAAALW77ZnZxlYRrZa4kruNZIxwJfTX')
    RECAPTCHA_PRIVATE_KEY= os.environ.get('6Leux-MiAAAAACB_LBJovYa4Ri_R4aFhpJot4p3JY')


