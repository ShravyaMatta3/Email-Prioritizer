from flask import Flask, redirect, request, session, url_for
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Google OAuth settings
GOOGLE_CLIENT_ID = 'YOUR_CLIENT_ID_HERE'
CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']

# Initialize the OAuth flow
flow = Flow.from_client_secrets_file(
    CLIENT_SECRET_FILE,
    scopes=SCOPES,
    redirect_uri='http://localhost:5000/callback'
)

@app.route('/')
def index():
    if 'email' in session:
        return redirect(url_for('dashboard'))
    else:
        return '<a href="/login">Login with Google</a>'

@app.route('/login')
def login():
    authorization_url, state = flow.authorization_url(access_type='offline')
    session['state'] = state
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    flow.fetch_token(authorization_response=request.url)
    if not session['state'] == request.args['state']:
        return 'Invalid state'
    id_info = id_token.verify_oauth2_token(flow.credentials._id_token, None)
    session['email'] = id_info['email']
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        return f'Logged in as: {session["email"]}'
    else:
        return 'Not logged in'

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
