from flask import render_template, request, redirect, url_for, current_app, send_from_directory
from . import main
from . import forms
import datetime
from .getshellsize import GetShellSize
import os
from werkzeug.utils import secure_filename
from ..models import Pic_Table, Fanshell_data, db
import hashlib


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


def write_uploadedfile(filename):
    pass


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
                pic = Pic_Table(filename=newfname, original_name=origin_fname)
                db.session.add(pic)  # 加照片信息
                db.session.commit()  # 提交数据
                mygss = GetShellSize(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], newfname))  # 照片识别类初始化，并加载照片
                ret, show, fans = mygss.auto_detect()
                if ret in (-1, 0, 1):
                    # -1 加载了照片但是未找到纸张0 找到纸张未检测到扇贝
                    mygss.save_pic(img=show, path=os.path.join(current_app.config['FINISHED_FOLDER'], newfname))
                    if ret == 1:
                        # 1 检测到了扇贝
                        for index, value in enumerate(fans):
                            fanshell = Fanshell_data(shell_no=index + 1, shell_height=value[0], shell_width=value[1], \
                                                     shell_similar=value[2], shell_area=value[3], pic=pic)
                            db.session.add(fanshell)
                        db.session.commit()
                else:
                    # -2 加载照片错误
                    pass
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    pagination = Pic_Table.query.order_by(Pic_Table.detectdate.desc(), Pic_Table.id.desc()).paginate(page, per_page=current_app.config['PICS_PER_PAGE'], error_out=False)
    pics = pagination.items
    return render_template('newindex.html', form=form, pics=pics, pagination=pagination)


@main.route('/export_xls', methods=['GET', 'POST'])
def export_xls():
    form = forms.xlsForm()
    if request.method == 'POST':
        selected = form.checked.data
        for sl in selected:
            pass
        return redirect(url_for('.export_xls'))
    page = request.args.get('page', 1, type=int)
    pagination = Pic_Table.query.order_by(Pic_Table.detectdate.desc(), Pic_Table.id.desc()).paginate(page, per_page=current_app.config['PICS_PER_PAGE'], error_out=False)
    pics = pagination.items
    return render_template('export_xls.html', form=form, pagination=pagination, pics=pics)


@main.route('/finished/<filename>')
def getfinishedpic(filename):
    return send_from_directory(current_app.config['FINISHED_FOLDER'], filename)


@main.route('/uploads/<filename>')
def getuploadedpic(filename):
    return send_from_directory(current_app.config['UPLOADED_PHOTOS_DEST'], filename)