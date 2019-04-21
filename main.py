from flask import Flask, request, redirect, render_template, session, flash
import cgi
#import os
# import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True


#app for sign up form
@app.route("/", methods=['GET', 'POST'])
def signup():
    if request.method =='POST':
        email = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
        if not is_email(email):
            flash('Rut-Roh... "' + email + '"might not be a <i>"REAL"</i> email address!')
            flash('Try Again!')
            return redirect('/')
        else:
            flash('You did a great job entering the right stuff!')



# app for success page
# @app.route("/success", methods=['GET', 'POST'])
# def winner():



def is_email(string):

    atsign_index = string.find('@')
    atsign_present = atsign_index >= 0
    if not atsign_present:
        return False
    else:
        domain_dot_index = string.find('.', atsign_index)
        domain_dot_present = domain_dot_index >= 0
        return domain_dot_present