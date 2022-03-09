from ensurepip import bootstrap
from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
#initialising application

app= Flask(__name__,instance_relative_config=True)
#setting up configuration

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initialise flask extension

bootstrap = Bootstrap(app)

from app import views