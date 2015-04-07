# -*- coding: UTF-8 -*- 

from flask import Module,render_template,jsonify, redirect, request,session,g
from testTeam.testteamconfig import *
from testTeam.services import userservice,projectservice
from testTeam.models.userprofile import UserStatus
from testTeam.controllers.filters import login_filter

project = Module(__name__)
project.before_request(login_filter)

@project.route('/Project')
def index():
    return render_template('Project/List.html')

@project.route('/Project/Create',methods=['POST'])
def create():
    projectservice.create(request.json['ProjectName'],request.json['Introduction'],g.user_id)
    return jsonify(created=True)
