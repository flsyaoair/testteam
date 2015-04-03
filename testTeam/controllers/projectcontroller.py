# -*- coding: UTF-8 -*- 

from flask import Module,render_template,jsonify, redirect, request,session
from testTeam.testteamconfig import *
from testTeam.services import userservice
from testTeam.models.userprofile import UserStatus

project = Module(__name__)

@project.route('/Project')
def index():
    return render_template('Project/List.html')
