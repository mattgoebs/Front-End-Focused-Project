from flask_app import app   
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.product_model import Product

@app.route('/log')
def log():
    return render_template('log.html')

@app.route('/users/register', methods=['POST'])
def register():
    if not User.validate(request.form):
        return redirect('/log')
    passwrd = request.form['password']
    data = {
        **request.form,
        'password': passwrd
    }
    id = User.create(data)
    session['user_id'] = id
    return redirect('/admin')

@app.route('/users/login', methods=['POST'])
def login():
    data = {'email' : request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Invalid login info', 'log')
        return redirect('/login')
    if not user_in_db.password:
        flash('Invalid login info', 'log')
        return redirect('/login')
    session['user_id'] = user_in_db.id
    return redirect('/')

@app.route('/gallery')
def productss():
    if 'user_id' not in session:
        return redirect('/login')
    all_product = Product.get_all()
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('gallery.html', all_product=all_product, logged_user=logged_user)