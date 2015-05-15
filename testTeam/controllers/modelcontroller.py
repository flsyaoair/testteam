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
    return render_template('Model/List.html',Project = project,title = project.ProjectName)

@model.route('/Model/Create',methods=['POST'])
def create():
    modelname = request.json["ModelName"]
    description = request.json["Description"]
    project = request.json["Project"]
    isExist = modelservice.create(modelname, description, project, g.user_id)
    return jsonify(isExist=isExist)

@model.route('/Model/Query',methods=['POST'])
def query():
    project = request.json["Project"]
    models = modelservice.query(project)
    models_dict_list = []
    for m in models:
        m_dict = {}
        m_dict.update(m.__dict__)
        m_dict["ProjectName"]=m.Project.ProjectName
        del m_dict["Project"]
        del m_dict["_sa_instance_state"]
        models_dict_list.append(m_dict)
    return jsonify(models=models_dict_list)