from flask import Flask
from flask_mail import Mail

from api.spotify import route as spotify
from api.email import route as email
from api.sheet import route as sheet
from credentials import MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD, MAIL_USE_TLS, MAIL_USE_SSL

app = Flask(__name__)
app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = MAIL_USE_SSL
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = MAIL_USERNAME

mail = Mail(app)

app.register_blueprint(spotify, url_prefix="/api/spotify")
app.register_blueprint(email, url_prefix="/api/email")
app.register_blueprint(sheet, url_prefix="/api/sheet")