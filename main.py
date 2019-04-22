from flask import Flask, request, redirect, render_template, session, flash
import cgi
# import os
# import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True


#app for sign up form
@app.route("/", methods=['GET', 'POST'])
def index():
    encoded_error = request.args.get("error")
    
    return render_template('index.html') #, signup=signup(), error=encoded_error and cgi.escape(encoded_error, quote=True)

@app.route("/", methods=['GET', 'POST'])
#def valid_signup():
        


def signup():
    #if request.method =='POST':
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    
    un_error = ''
    pw_error = ''
    verify_error = ''
    email_fail = ''

    if len(username) <= 4 or len(username) >= 20:
        un_error = "Oopsies!  Please enter a valid email."
        flash(un_error)
            
    if len(password) == 0:
        pw_error = 'You need to add a password.'
        flash(pw_error)
    elif len(password) <= 4 or len(password) >= 20:
        pw_error = 'Please enter a valid password'
        flash(pw_error)

    if verify != password:
        verify_error = 'These passwords do not match. Make them the same, and write them down somewhere so you do not forget'
        flash(verify_error)
        
    if not is_email(email):
        flash('Rut-Roh... "' + email + '"might not be a <i>"REAL"</i> email address!')

        #return redirect('/')
    else:
        flash('You did a great job entering the right stuff!')

#@app.before_request
#def require_signup():
#    return redirect("/signup")

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


app.secret_key = 'A0Qr978j/3AyX Rob~XHeeH!j23mN]L43WX/,?RU'

if __name__ == "__main__":

    app.run()