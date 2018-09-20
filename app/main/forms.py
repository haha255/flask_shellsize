from flask_wtf import FlaskForm
from wtforms import MultipleFileField, BooleanField, SubmitField
from flask_wtf.file import FileAllowed, FileRequired


class picForm(FlaskForm):
    pics = MultipleFileField('选择图片', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])


class xlsForm(FlaskForm):
    checked = BooleanField('选择')
    makexls = SubmitField('生成并下载')