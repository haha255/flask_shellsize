from flask_wtf import FlaskForm
from wtforms import SubmitField, MultipleFileField
from flask_wtf.file import FileAllowed, FileRequired


class picForm(FlaskForm):
    pics = MultipleFileField('选择图片', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('测算')

