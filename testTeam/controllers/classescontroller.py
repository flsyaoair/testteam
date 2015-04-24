# -*- coding: UTF-8 -*- 
from flask import Module,render_template,jsonify, redirect, request,session,g
from testTeam.testteamconfig import *
from testTeam.controllers.filters import login_filter
from testTeam.services import classesservice, projectservice

classes = Module(__name__)
classes.before_request(login_filter)

@classes.route('/Classes/Create',methods=['POST'])
def create():
    classname = request.json['Name']
    projects = request.json['Project']
    isexist = classesservice.isexist(classname)
    if not isexist:
        if len(projects) != 0:
            for project in projects:
                classesservice.create(classname,project,g.user_id)
        else:
            classesservice.create(classname,None,g.user_id)
#     existname = classesservice.get_name()
# 
#     if not classname in existname:
#         isexist = False
#         for project in projects:
#             classesservice.create(classname,project,g.user_id)
#     else:
#         isexist = True
    return jsonify(isexist=isexist)

@classes.route('/Classes/Query',methods=['POST'])
def query():
    classes = classesservice.query()
    class_list = []
    for c in classes:
        dict = {}
        dict.update(c.__dict__)
        del dict["_sa_instance_state"]
        class_list.append(dict)
        
    return jsonify(class_list = class_list)

# @classes.route('/Classes/Filter',methods=['POST'])
# def filter():
#     class_name = request.json['ClassName']
#     subprojects = projectservice.querysub(class_name,'LastUpdateDate',g.user_id)
#     return jsonify(filterd = True)

@classes.route('/Classes/Update',methods=['POST'])
def update():
    oldname = request.json['OldName']
    newname = request.json['NewName']
    projectlist = request.json['Project']
    
    return jsonify(updated = True)