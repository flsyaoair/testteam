# -*- coding: UTF-8 -*- 
from flask import Module,render_template,redirect,request,session,jsonify,g
from testTeam.services import userservice
from testTeam.controllers.filters import login_filter

user = Module(__name__)
user.before_request(login_filter)

@user.route('/logout')
def logout():
    response = redirect('/')
    session['username'] = None
    session['userid'] = None
    return response

@user.route('/Profile')
def profile():
    u = userservice.get(session['username'])
    return render_template('Profile/Detail.html',User=u)

@user.route('/UpdateProfile',methods=['POST'])
def update_profile():
    email = request.json['Email']
    nick = request.json['Nick']
    updated = userservice.udpate_profile(email,nick,g.user_id)
    if updated:
        session['username'] = email
    return jsonify(Updated=updated)