from flask import Flask, flash, request, render_template, redirect, session, url_for
from app import app, login_required

@app.route('/')
def home():
    return render_template('/content/home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('you were just logged in!')
            return redirect(url_for('home'))
    return render_template('/content/login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('you were just logged out!')
    return redirect(url_for('home'))
    
@app.route('/register')
def register():
    return render_template('/content/register.html')

@app.route('/<category>')
def posts(category):
    return render_template('/content/posts.html', category=category)
    
@app.route('/view/<int:post_id>')
def view(post_id):
    return render_template('/content/view.html')

@app.route('/<category>/edit', methods=['GET', 'POST'])
def edit(category):
    if request.method == 'GET':
        return render_template('/content/edit.html', cat=category)
    elif request.method == 'POST':
        listings = {
            'subject': request.form['subject'],
            'region': request.form['region'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'body': reqwuest.form['body'],
            'homes_type': request.form['homes_type'],
            'homes_price': request.form['homes_price'],
            'homes_bedrooms': request.form['homes_bedrooms'],
            'homes_parking': request.form['homes_parking'],
            'homes_year': request.form['homes_year'],
            'homes_sqft': request.form['homes_sqft'],
        }
        # store data in data store
        # code
        # code 
        return render_template('/content/view.html', cat=category, posts=posts)
    else:
        return render_template(error_page.html)
        