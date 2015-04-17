# -*- coding: UTF-8 -*- 
from flask import Module,render_template,jsonify, redirect, request,session,g
from testTeam.testteamconfig import *
from testTeam.controllers.filters import login_filter
from testTeam.services import classesservice

classes = Module(__name__)
classes.before_request(login_filter)

@classes.route('/Classes/Create',methods=['POST'])
def create():
    classname = request.json['Name']
    projects = request.json['Project']
    for project in projects:
        classesservice.create(classname,project,g.user_id)
    return jsonify(created=True)