# -*- coding: UTF-8 -*- 

from flask import Module,render_template,jsonify, redirect, request,session,g
from testTeam.testteamconfig import *
from testTeam.controllers.filters import login_filter

case = Module(__name__)
case.before_request(login_filter)

@case.route('/CreatCase/1')
def creat():
    return render_template('Case/Create.html')

@case.route('/Case/1')
def detail():
    return render_template('Case/Detail.html')