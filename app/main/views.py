from flask import render_template, request, redirect, url_for
from . import main
from . import forms
# from .. import db


@main.route('/', methods=['GET', 'POST'])
def index():
    form = forms.picForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            pass
        return redirect(url_for('.index'))
    return render_template('index.html', form=form)


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
