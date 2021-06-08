from market import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = item.query
    return render_template('market.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                            email_address=form.email_address.data,
                             password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
         attempted_user = User.query.filter_by(username=form.username.data).first()
         if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
             login_user(attempted_user)
             flash(f'Success! You are logged in as { attempted_user.username}', category='success')
             return redirect(url_for('market_page'))
         else:
             flash(f'Username and password does not match')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home"))