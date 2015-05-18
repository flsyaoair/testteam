# -*- coding: UTF-8 -*- 
from testTeam.models import Member,database
from datetime import datetime

def get(projectId):
    session = database.get_session()
    members = session.query(Member).filter(Member.ProjectId==projectId).all()
    session.close()
    return members