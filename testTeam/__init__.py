# -*- coding: UTF-8 -*- 

from flask import Flask
from testTeam.controllers import *

def create_testTeam_app():
    app = Flask(__name__)
    app.jinja_env.variable_start_string = '(('
    app.jinja_env.variable_end_string = '))'
    app.config.from_pyfile('testteamconfig.py')
    app.register_module(home)
    
    return app