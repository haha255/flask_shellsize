import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1qazxsw2!@'  # 取环境变量的密码或者自己规定的密码
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'uploads')  # 文件上传路径
    FINISHED_FOLDER = os.path.join(basedir, 'uploads/finished')  # 文件识别后保存的路径
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])  # 允许上传的文件类型。
    DEBUG = True
    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'fanshells.sqlite')

config = {
    'development': ProductionConfig,
    'default': ProductionConfig,
}
