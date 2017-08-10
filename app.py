#!/usr/bin/python

from flask import Flask, render_template, request, Response, flash, redirect, url_for, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from dbfunctions import *
import json
import sys, os
import pymysql
import pprint
from operator import itemgetter, attrgetter, methodcaller

app = Flask(__name__)
app.secret_key= os.urandom(24)

@app.route("/")
@app.route("/index")
def index():
	return render_template('home.html')


class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min=1, max=50)])
	username = StringField('Username', [validators.Length(min=4, max=25)])
	email = StringField('Email', [validators.Length(min=6, max=50)])
	password = PasswordField('Password', [
		validators.DataRequired(),
		validators.EqualTo('confirm', message='Passwords do not match')
	])
	confirm = PasswordField('Confirm Password')


# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		name = form.name.data
		email = form.email.data
		username = form.username.data
		password = sha256_crypt.encrypt(str(form.password.data))

		credentials = { 'name' : name,
						'email' : email,
						'username' : username,
						'password' : password
					}

		createUser(**credentials)

		flash('You are now registered and can log in', 'success')

		return redirect(url_for('login'))
	return render_template('register.html', form=form)

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		# Get Form Fields
		username = request.form['username']
		password_candidate = request.form['password']

		loginInfo = {
		'username' : username,
		'password' : password_candidate
		}

		# Get user by username
		try:
			user = getUser(**loginInfo)
		except TypeError as error:
			error = 'User does not exsit'
			return render_template('register.html', error=error)
		else:
			username, password = getUser(**loginInfo)

		# Compare Passwords
		if sha256_crypt.verify(password_candidate, password):
			# Passed
			session['logged_in'] = True
			session['username'] = username

			flash('You are now logged in', 'success')
			return redirect(url_for('market'))
		else:
			error = 'Invalid login'
			return render_template('login.html', error=error)


	return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Unauthorized, Please login', 'danger')
			return redirect(url_for('login'))
	return wrap

# Logout
@app.route('/logout')
@is_logged_in
def logout():
	session.clear()
	flash('You are now logged out', 'success')
	return redirect(url_for('login'))


@app.route('/market', methods=['GET', 'POST'])
def selectItems():
	if request.method == 'POST':
		has_items = request.form.getlist('has')
		want_items = request.form.getlist('want')
		print(has_items)
		print(want_items)
		market = []
		for i in has_items:
			for j in want_items:
				items = getTrade(i, j)
				market.extend(items)
		market = sorted(market, key=itemgetter(8), reverse=True)
		return render_template('market.html', market=market)
		# for has_index in has_items:
		# 	has_items[has_index]
	return render_template('market.html')

@app.route('/save', methods=['GET', 'POST'])
def saveItems():
	if request.method == 'POST':
			has_items = request.form.getlist('has')
			want_items = request.form.getlist('want')
			user = session['username']
			description = request.form['description']
			saveBarter(user, description)
			for i in has_items:
				save_has_items = saveHasItem(i, user)
			for i in want_items:
				save_want_items = saveWantItem(i, user)
			# barter = lookupBarter(user, description)
			return render_template('market.html')
	return render_template("market.html")



# used for debugging in development only!  NOT for production!!!
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
