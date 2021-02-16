from flask import render_template, flash, redirect
from flask.globals import request
from flask.helpers import url_for
from flask_login import login_required, current_user, login_user, logout_user

from app import APP, login_manager,db
from app.forms import LoginForm, RegistrationForm
from app.models import User


@login_manager.user_loader
def loader(idt):
    return User.query.get(int(idt))

@APP.route('/')
def home():
    return render_template('index.html', title='Index')


@APP.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html', title='welcome')


@APP.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('welcome'))
    form = LoginForm()
    if (form.validate_on_submit()):
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not form.password.data == user.password:
            # flash(f'Invalid username or password')
            redirect(url_for('login'))
        login_user(user)
        # flash(f'{form.username.data} logged in')
        next_page = request.args.get('next')
        if not next_page:
            next_page = url_for('welcome')
        return redirect(next_page)
    print("NO use")
    return render_template('login.html', form=form, title='Login')

@APP.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@APP.route('/signup', methods=['POST', 'GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form, title='Sign UP')