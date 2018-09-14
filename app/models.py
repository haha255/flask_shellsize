from . import db


class Pic_Table(db.Model):
    __tablename__ = 'pic_table'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(64), unique=True)
    filedate = db.Column(db.DateTime)  # 文件生成的时间
    detectdate = db.Column(db.DateTime)  # 检测扇贝的时间
    fanshells = db.relationship('Fanshell_data', backref='pic_table')

    def __repr__(self):
        return '<Filename: %r>' % self.filename


class Fanshell_data(db.Model):
    __tablename__ = 'fanshell_data'
    id = db.Column(db.Integer, primary_key=True)
    shell_no = db.Column(db.Integer)  # 一张纸上的扇贝编号
    shell_height = db.Column(db.Integer)  # 扇贝的高
    shell_width = db.Column(db.Integer)  # 扇贝的宽度
    shell_similar = db.Column(db.Numeric(3, 2))  # 扇贝的相似度
    shell_area = db.Column(db.Integer)  # 扇贝的面积
    pic_id = db.Column(db.Integer, db.ForeignKey('pic_table.id'))

    def __repr__(self):
        return '<Shell No:%d Height:%d Width:%d>' % (self.shell_no, self.shell_height, self.shell_width)

