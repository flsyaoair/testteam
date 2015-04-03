# -*- coding: UTF-8 -*- 

from flask import Module,render_template,jsonify, redirect, request,session
from testTeam.testteamconfig import *
from testTeam.services import userservice
from testTeam.models.userprofile import UserStatus

home = Module(__name__)


@home.route('/')
def index():
    if 'username' in session and not session['username'] == None:
        return redirect('/Project')
    return render_template('Login.html',
                           title = u'登陆'
                           )

@home.route('/Login',methods=['POST'])
def login():
    email = request.json['Email']
    password = request.json['Password']
    user = userservice.get(email)
    if user == None:
        response = jsonify(isDisabled = False,isMatch=False)
        return response

    if user.Status == UserStatus.Disabled:
        response = jsonify(isDisabled = True,isMatch=None)
        return response

    if not user.Password == password:
        response = jsonify(isDisabled = False,isMatch=False)
        return response

    session['userid'] = user.UserId
    session['username'] = user.Email
    session['isadmin'] = user.IsAdmin
    response = jsonify(isDisabled=False,isMatch=True)
    return response

@home.route('/Register')
def register():
    return render_template('Register.html',
                           title = u'注册')

@home.route('/Register/Save',methods=['POST'])
def save():
    (exist,userid) = userservice.register(request.json['Email'],request.json['Nick'],request.json['Password'])

    if not exist:
        session['userid'] = userid
        session['username'] = request.json['Email']
    session['isadmin'] = False
    result = {'created' : not exist}
    return jsonify(result)

@home.route('/logout')
def logout():
    response = redirect('/')
    session['username'] = None
    session['userid'] = None
    return response
    
