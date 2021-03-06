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
    projects = projects if (len(projects) != 0) else []
    isexist = classesservice.isexist(classname)
    if not isexist:
        classesservice.create(classname,projects,g.user_id)
#         if len(projects) != 0:
#                 classesservice.create(classname,projects,g.user_id)
#         else:
#             classesservice.create(classname,None,g.user_id)
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

@classes.route('/Classes/Update',methods=['POST'])
def update():
    oldname = request.json['OldName']
    newname = request.json['NewName']
    newprojects = request.json['Project']
    classesservice.update(oldname, newname, newprojects, session['userid'])
    
    return jsonify(updated = True)

@classes.route('/Classes/Delete',methods=['POST'])
def delete():
    class_name = request.json["Name"]
    classesservice.delete(class_name)

    return jsonify(deleted = True)