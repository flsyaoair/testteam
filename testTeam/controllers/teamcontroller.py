# -*- coding: UTF-8 -*- 
from flask import Module,jsonify, request,g
from testTeam.testteamconfig import *
from testTeam.services import teamservice
from testTeam.controllers.filters import login_filter

team = Module(__name__)
team.before_request(login_filter)

@team.route('/Team/QueryTeam',methods=['POST'])
def queryTeam():
    projectId = request.json['ProjectId']
    memberList = teamservice.get(projectId)
    members = teamservice.objList_To_DictList(memberList)
    allMemberList = teamservice.getAll(projectId)
    allMembers = teamservice.objList_To_DictList(allMemberList)

    return jsonify(members = members, allMembers = allMembers)

@team.route('/Team/RemoveMember',methods=['POST'])
def removeMember():
    projectId = request.json['ProjectId']
    userId = request.json['UserId']
    teamservice.removeUser(projectId, userId)
    
    return jsonify(isRemoved = True)

@team.route('/Team/AddMember',methods=['POST'])
def addMember():
    projectId = request.json['ProjectId']
    email = request.json['Email']
    teamservice.addUser(projectId, email)
    
    return jsonify(isAdded = True)