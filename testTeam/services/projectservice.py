# -*- coding: UTF-8 -*- 
from testTeam.models import Project, database, Member, Classes
from datetime import datetime

def get(projectid):
    session = database.get_session()
    project = session.query(Project).filter(Project.ProjectId == projectid).one()
    session.close()
    return project

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
    session.close()
    
def query(page_no,page_size,order_by,current_user,class_name):
    session = database.get_session()
    
    projectid_list = session.query(Member.ProjectId).filter(Member.UserId == current_user)
    subdata = ""
    subdata_list = []
    if class_name != "all":
        subdata = session.query(Classes.ProjectId).filter(Classes.ClassName == class_name).all()
        for i in subdata:
            subdata_list.append(i[0])

    project_list = session.query(Project).filter(Project.ProjectId.in_(projectid_list))    
    (data,row_count,page_count,page_no) = database.query_more(project_list,order_by,page_no,page_size)
    
    session.close()
    return (data,subdata_list,row_count,page_count,page_no)

# def querysub(class_name,order_by,current_user):
#     session = database.get_session()
#     subprojects_id = session.query(Classes.ProjectId).filter(Classes.ClassName = class_name)
#     subproject_list = session.query(Project).filter(Project.ProjectId.in_(subprojects_id))