import os

from flask import Flask

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config['SECRET_KEY'] = os.environ.get("APP_CONFIG_SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("APP_CONFIG_DATABASE_URI")