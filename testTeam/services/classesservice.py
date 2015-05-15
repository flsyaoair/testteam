# -*- coding: UTF-8 -*- 
from testTeam.models import database, Classes
from datetime import datetime

def create(classname,projects,creator):
    if projects != []:
        for project in projects:
            create_one(classname, project, creator)
    else:
        projects = None
        create_one(classname, projects, creator)
    
def create_one(classname,project,creator):
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
    
# def get_name():
#     session = database.get_session()
#     existname = session.query(Classes).all()
#     namelist = []
#     for i in existname:
#         namelist.append(i.ClassName)
#         
#     return namelist

def isexist(classname):
    session = database.get_session()
    existcount = session.query(Classes).filter(Classes.ClassName == classname).count()
    session.close()
    if existcount > 0:
        return True
    else:
        return False
    
def query():
    session = database.get_session()
    classlist = session.query(Classes).all()
    class_list = []
    name_list = []
    for i in classlist:
        if not i.ClassName in name_list:
            class_list.append(i)
            name_list.append(i.ClassName)
    return class_list

def delete(class_name):
    session = database.get_session()
    session.query(Classes).filter(Classes.ClassName == class_name).delete()
    session.commit()
    session.close()
    
def update(oldname,newname,newprojects,creator):
    delete(oldname)
    create(newname, newprojects, creator)
    
    
    