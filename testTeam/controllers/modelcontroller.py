# -*- coding: UTF-8 -*- 
from flask import Module,render_template,jsonify, redirect, request,session,g
from testTeam.testteamconfig import *
from testTeam.services import userservice,projectservice
from testTeam.models.userprofile import UserStatus
from testTeam.controllers.filters import login_filter

model = Module(__name__)
model.before_request(login_filter)

@model.route('/Project/Model/1')
def index():
    return render_template('Model/List.html')