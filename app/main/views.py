from flask import render_template, request, redirect, url_for
from . import main
# from .. import db


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('.index'))
    return render_template('index.html')
