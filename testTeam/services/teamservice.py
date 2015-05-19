# -*- coding: UTF-8 -*- 
from testTeam.models import Member,database, UserProfile
from datetime import datetime
from testTeam.services import userservice
from sqlalchemy.sql.elements import not_

def objList_To_DictList(objList):
    DictList = []
    for o in objList:
        dict = {}
        dict.update(o.__dict__)
#         dict["Email"] = o.User.Email
#         dict["User"] = o.User.Nick
        del dict["_sa_instance_state"]
        DictList.append(dict)
    return DictList

def get(projectId):
    session = database.get_session()
    memberInProject = session.query(Member.UserId).filter(Member.ProjectId==projectId)
    members = session.query(UserProfile).filter(UserProfile.UserId.in_(memberInProject))
    session.close()
    return members

def getAll(projectId):
    session = database.get_session()
    memberInProject = session.query(Member.UserId).filter(Member.ProjectId==projectId)
    members = session.query(UserProfile).filter(not_(UserProfile.UserId.in_(memberInProject)))
    session.close()
    return members

def removeUser(projectId,userId):
    session = database.get_session()
    session.query(Member).filter(Member.ProjectId==projectId).filter(Member.UserId==userId).delete()
    session.commit()
    session.close()
    
def addUser(projectId,email):
    session = database.get_session()
    user = userservice.get(email)

    member = Member()
    member.ProjectId = projectId
    member.UserId = user.UserId

    session.add(member)
    session.commit()
    session.close()