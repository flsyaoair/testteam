# -*- coding: UTF-8 -*- 
from testTeam.models import Project, database, Member
from datetime import datetime

def create(project_name,project_introduction,creator):
    session = database.get_session()
    p = Project()
    p.ProjectName = project_name.strip()
    p.Creator = creator
    p.CreateDate = datetime.now()
    p.LastUpdateDate = datetime.now()
    p.Introduction = project_introduction
    
    m = Member()
    m.UserId = creator
    p.Members.append(m)

    session.add(p)
    session.commit()