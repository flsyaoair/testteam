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
    (data,row_count,page_count,page_no) = projectservice.query(1,PAGESIZE_project,'LastUpdateDate',g.user_id)

    return render_template('Project/List.html',projects=data.all())

@project.route('/Project/Create',methods=['POST'])
def create():
    projectservice.create(request.json['ProjectName'],request.json['Introduction'],g.user_id)
    return jsonify(created=True)

@project.route('/Project/Query',methods=['POST'])
def query():
    page_no = request.json['PageNo']
    (data,row_count,page_count,page_no) = projectservice.query(page_no,PAGESIZE_project,'LastUpdateDate',g.user_id)
    projects = []
    for p in data.all():
        projects.append({'ProjectId':p.ProjectId,'ProjectName':p.ProjectName,'Introduction':p.Introduction,'CreateDate':p.CreateDate.isoformat(),'LastUpdateDate':p.LastUpdateDate.isoformat(),'Creator':p.UserProfile.Nick})
    return jsonify(data=projects,row_count=row_count,page_count=page_count,page_no=page_no)