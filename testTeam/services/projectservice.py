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
    
def query(page_no,page_size,order_by,current_user):
    session = database.get_session()
    projectid_list = session.query(Member.ProjectId).filter(Member.UserId == current_user)
    project_list = session.query(Project).filter(Project.ProjectId.in_(projectid_list))
    (data,row_count,page_count,page_no) = database.query_more(project_list,order_by,page_no,page_size)
    
    session.close()
    return (data,row_count,page_count,page_no)