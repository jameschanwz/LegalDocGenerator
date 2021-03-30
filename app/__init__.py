from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_mail import Mail

app = Flask(__name__)
bootstrap = Bootstrap(app)
mail = Mail(app)
app.config.from_object(Config)

from app import routes,email
