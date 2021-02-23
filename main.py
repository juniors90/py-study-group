"""

PROJECT: "Imagine a Github Profile Finder"

AUTHOR: juniors

CREATED AT: 22/02/2021

"""
from datetime import datetime
import requests
from flask import Flask, render_template, request, redirect, url_for
from forms import SearchProfileForm

app = Flask(__name__)
app.config['SECRET_KEY'] ='a-secret-key'


# public index endpoint
# ---------------------

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchProfileForm()
    if form.validate_on_submit():
        username = form.username.data
        response = requests.get(f'https://api.github.com/users/{username}')

        if response.status_code == 200:

            profile = response.json()

            date = datetime.strptime(profile['created_at'], "%Y-%m-%dT%H:%M:%SZ").date().strftime("%d/%m/%y")
            
            next = request.args.get('next', None)

            if next:
                return redirect(next)

            return render_template('index.html',
                                    name=username,
                                    profile=profile,
                                    date=date, form=form)
        else:
            # if the response.status_code is 404
            return redirect(url_for('error'))

    return render_template('index.html', form=form)

# error endpoint
# -------------------------

@app.route('/error')
def error():
    return render_template('404.html')

# register error handlers
# -------------------------

@app.errorhandler(500)
def base_error_handler(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def error_404_handler(e):
    return render_template('404.html'), 404
