from flask import Flask, render_template, request, jsonify, redirect
import json
from GoogleAccesser import GoogleAccesser
from functools import wraps

from os import environ as env
from werkzeug.exceptions import HTTPException
from flask import session
from flask import url_for
from authlib.flask.client import OAuth
from six.moves.urllib.parse import urlencode
import os

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

AUTH0_CALLBACK_URL = os.environ['AUTH0_CALLBACK_URL']
AUTH0_CLIENT_ID = os.environ['AUTH0_CLIENT_ID']
AUTH0_CLIENT_SECRET = os.environ['AUTH0_CLIENT_SECRET']
AUTH0_DOMAIN = os.environ['AUTH0_DOMAIN']
AUTH0_BASE_URL = 'https://' + AUTH0_DOMAIN
AUTH0_AUDIENCE = ""
if AUTH0_AUDIENCE is '':
    AUTH0_AUDIENCE = AUTH0_BASE_URL + '/userinfo'

app = Flask(__name__, template_folder="templates/")
app.secret_key = "secretvery"
app.debug = True


@app.errorhandler(Exception)
def handle_auth_error(ex):
    response = jsonify(message=str(ex))
    response.status_code = (ex.code if isinstance(ex, HTTPException) else 500)
    return response


oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    api_base_url=AUTH0_BASE_URL,
    access_token_url=AUTH0_BASE_URL + '/oauth/token',
    authorize_url=AUTH0_BASE_URL + '/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)


def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if 'profile' not in session:
      # Redirect to Login page here
      return redirect('/login')
    return f(*args, **kwargs)

  return decorated


@app.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session.
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    return render_template('index.html')


@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri=AUTH0_CALLBACK_URL, audience=AUTH0_AUDIENCE)


@app.route('/logout')
def logout():
    session.clear()
    params = {'returnTo': url_for('home', _external=True), 'client_id': AUTH0_CLIENT_ID}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

@app.route('/')
@requires_auth
def index():
    return render_template('index.html')

@app.route('/square/', methods=['POST'])
def square():
    num = float(request.form.get('number', 0))
    squareNum = num ** 2
    data = {'square': squareNum}
    data = jsonify(data)
    return data


@app.route('/apikey1/', methods=['POST'])
def apikey1():
    apiKey = str(request.form.get('apinumber', 0))
    searchQuery = str(request.form.get('apinumber1', 0))
    print(apiKey)
    print(searchQuery)

    cardName = GoogleAccesser(apiKey, searchQuery)

    data = {'cardName': cardName}
    data = jsonify(data)
    return data


if __name__ == '__main__':
    app.run(debug=True)
