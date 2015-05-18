# -*- coding: UTF-8 -*- 

from flask import Module,render_template,jsonify, redirect, request, session, g
from testTeam.testteamconfig import *
from testTeam.services import caseservice
from testTeam.controllers.filters import login_filter

case = Module(__name__)
case.before_request(login_filter)

@case.route('/CreateCase/1')
def creat():
    return render_template('Case/Create.html')

@case.route('/Case/1')
def detail():
    return render_template('Case/Detail.html')

@case.route('/Case/1',methods=['POST'])
def create_case():
    caseservice.create_case(request.json['case_name'],request.json['description'],request.json['versions'],request.json['caseurl'],g.user_id)
    return jsonify(created=True)

@case.route('/Case/1',methods=['POST'])
def query_case():
    page_no = request.json['PageNo']
    (data,row_count,page_count,page_no) = query_case(page_no,PAGESIZE_case,'CreateDate',g.user_id,p.ProjectId)
    cases = []
    for p in data.all():
      cases.append({'CaseId':p.CaseId,'CaseName':p.CaseName,'Description':p.Description,'CreateDate':p.CreateDate.isoformat(),'LastUpdateDate':p.LastUpdateDate.isoformat(),'Versions':p.Versions,'CaseURL':p.CaseURL,'Creator':p.UserProfile.Nick})

    return jsonify(data=cases,row_count=row_count,page_count=page_count,page_no=page_no)

@case.route('/Case/1',methods=['POST'])
def del_case():
    caseservice.del_case(request.json['CaseId'])
    return jsonify(deleted=True)

@case.route('/Case/1',methods=['POST'])
def udpate_case():
    caseservice.udpate_case(request.json['case_name'],request.json['description'],request.json['versions'],request.json['Case_Id'])
    return jsonify(updated=True)