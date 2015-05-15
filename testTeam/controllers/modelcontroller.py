# -*- coding: UTF-8 -*- 
from flask import Module,render_template,jsonify, redirect, request,session,g
from testTeam.testteamconfig import *
from testTeam.services import modelservice,projectservice
from testTeam.models.userprofile import UserStatus
from testTeam.controllers.filters import login_filter

model = Module(__name__)
model.before_request(login_filter)

@model.route('/Model/<int:project_id>')
def index(project_id):
    project = projectservice.get(project_id)
    return render_template('Model/List.html',Project = project)

@model.route('/Model/Create',methods=['POST'])
def create():
    modelname = request.json["ModelName"]
    description = request.json["Description"]
    project = request.json["Project"]
    isExist = modelservice.create(modelname, description, project, g.user_id)
    return jsonify(isExist=isExist)