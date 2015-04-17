# -*- coding: UTF-8 -*- 
from testTeam.models import Project, database, Member, Classes
from datetime import datetime

def create(classname,project,creator):
    session = database.get_session()
    
    c = Classes()
    c.ClassName = classname.strip()
    c.Creator = creator
    c.ProjectId = project
    c.CreateDate = datetime.now()
    c.LastUpdateDate = datetime.now()
    
    session.add(c)
    session.commit()
    session.close()
    
def get_name():
    session = database.get_session()
    existname = session.query(Classes).all()
    namelist = []
    for i in existname:
        namelist.append(i.ClassName)
        
    return namelist