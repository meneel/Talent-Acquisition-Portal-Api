# -*- encoding: utf-8 -*-

"""Main Package for Controlling the API"""

from flask import Flask
from flask_bcrypt import Bcrypt # Bcrypt hashing for Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message

from .config import config_by_name
from app.main._base_model_class import *

db = SQLAlchemy(model_class = ModelClass)
flask_bcrypt = Bcrypt() # bcrypt hashing utilities
app = Flask(__name__)

def create_app(config_name : str):
    """Creates Flask Application

    :type  config_name: str
    :param config_name: Configuration for Setting up the Environment, can be
                        any of the following: ['dev', 'test', 'prod']
    """
    
    
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    
    

    return app


app.config['MAIL_SERVER'] = "mail.inspirigenceworks.com"
# app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "info@inspirigenceworks.com"
app.config['MAIL_PASSWORD'] = "007sun007Maa#"
mail = Mail(app)


def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    mail.send(msg)

    return "Please check your inbox"