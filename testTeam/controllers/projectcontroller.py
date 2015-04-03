# -*- coding: UTF-8 -*- 

from flask import Module,render_template,jsonify, redirect, request,session,g
from testTeam.testteamconfig import *
from testTeam.services import userservice
from testTeam.models.userprofile import UserStatus

project = Module(__name__)

@project.route('/Project')
def index():
    return render_template('Project/List.html')

#@project.route('/Project/Create',methods=['POST'])
#def create():
#
#    if (request.json['ProjectName'] != ''):
#        exist = projectservice.create(request.json['ProjectName'],g.user_id)
#    else :
#        exist = True
#    exist_json = {'exist': exist}
#    return jsonify(exist_json)
