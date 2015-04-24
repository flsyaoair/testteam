# -*- coding: UTF-8 -*- 

from flask import Module,render_template,jsonify, request,g
from testTeam.testteamconfig import *
from testTeam.services import projectservice
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

@project.route('/Project/Query',methods=['POST'])
def query():
    page_no = request.json['PageNo']
    class_name = request.json['ClassName']
    checked_list = request.json['CheckedList']
    (data,subdata,row_count,page_count,page_no) = projectservice.query(page_no,PAGESIZE_project,'LastUpdateDate',g.user_id,class_name)
    projects = []
    for p in data.all():
        if subdata == []:
#             isChecked = True if p.ProjectId in subdata else False
            isChecked = False
            if p.ProjectId in checked_list:
                isChecked = True
            projects.append({'ProjectId':p.ProjectId,'ProjectName':p.ProjectName,'Introduction':p.Introduction,'CreateDate':p.CreateDate.isoformat(),'LastUpdateDate':p.LastUpdateDate.isoformat(),'Creator':p.UserProfile.Nick,'IsChecked':isChecked})
        else :
            if p.ProjectId in subdata:
                projects.append({'ProjectId':p.ProjectId,'ProjectName':p.ProjectName,'Introduction':p.Introduction,'CreateDate':p.CreateDate.isoformat(),'LastUpdateDate':p.LastUpdateDate.isoformat(),'Creator':p.UserProfile.Nick})
    
    return jsonify(data=projects,row_count=row_count,page_count=page_count,page_no=page_no)