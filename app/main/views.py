from flask import render_template, request, redirect, url_for, current_app
from . import main
from . import forms
import datetime
import cv2
from .getshellsize import GetShellSize
import os
from werkzeug.utils import secure_filename
# from .. import db


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@main.route('/', methods=['GET', 'POST'])
def index():
    form = forms.picForm()
    if request.method == 'POST':
        files = form.pics.data
        for file in files:
            if file and allowed_file(file.filename):
                origin_fname = secure_filename(file.filename)  # 记录原始文件名,安全的。
                ext = origin_fname.rsplit('.', 1)[1].lower()  # 获取文件名后缀
                newfname = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + '.' + ext  # 新文件名
                file.save(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], newfname))
                mygss = GetShellSize()  # 照片识别类初始化
                img = mygss.loadPic(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], newfname))
                ret, approx, box = mygss.detect_rect(img)
                if ret:
                    dst = mygss.transform(img, approx, box)
                    sd, final = mygss.detect_shell(dst)
                    if len(sd) > 0:
                        xx, yy = 10, 20
                        for index, value in enumerate(sd):
                            text = 'No:{0}: Height={1:.1f}mm, Width={2:.1f}mm, Similar={3:.1%}, Area={4:.1f}cm2'.format\
                                    (index + 1, value[0], value[1], value[2], value[3])
                            cv2.putText(final, text, (xx, yy), cv2.FONT_HERSHEY_TRIPLEX, 0.6, (255, 0, 0))
                            yy += 25
                        cv2.imwrite(os.path.join(current_app.config['FINISHED_FOLDER'], newfname), final)
                    else:
                        print('没有检测到扇贝！')
                else:
                    print('没有检测到纸张！')
        return redirect(url_for('.index'))
    return render_template('newindex.html', form=form)


@main.route('/ex2', methods=['GET', 'POST'])
def example_2():
    if request.method == 'POST':
        pass
    return render_template('example_2.html')


@main.route('/ex3', methods=['GET', 'POST'])
def example_3():
    if request.method == 'POST':
        pass
    return render_template('example_3.html')


@main.route('/ex4', methods=['GET', 'POST'])
def example_4():
    if request.method == 'POST':
        pass
    return render_template('example_4.html')


@main.route('/ex5', methods=['GET', 'POST'])
def example_5():
    if request.method == 'POST':
        pass
    return render_template('example_5.html')


@main.route('/ex6', methods=['GET', 'POST'])
def example_6():
    if request.method == 'POST':
        pass
    return render_template('example_6.html')


@main.route('/ex7', methods=['GET', 'POST'])
def example_7():
    if request.method == 'POST':
        pass
    return render_template('example_7.html')


@main.route('/ex8', methods=['GET', 'POST'])
def example_8():
    if request.method == 'POST':
        pass
    return render_template('example_8.html')
