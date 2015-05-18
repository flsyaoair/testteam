# -*- coding: UTF-8 -*- 
from testTeam.models import database, Model
from datetime import datetime

def create(modelname,description,project,creator):
    
    isExist = isexist(modelname,project)
    if not isExist:
        session = database.get_session()
        m = Model()
        m.ModelName = modelname.strip()
        m.Description = description
        m.ProjectId = project
        m.Creator = creator
        m.CreateDate = datetime.now()
        m.LastUpdateDate = datetime.now()
        session.add(m)
        session.commit()
        session.close()
        
    return isExist

def isexist(modelname,projectid):
    session = database.get_session()
    existcount = session.query(Model).filter(Model.ProjectId == projectid).filter(Model.ModelName == modelname).count()
    session.close()
    isExist = True if existcount > 0 else False
    return isExist

def query(projectid):
    session = database.get_session()
    if projectid != 'all':
        models = session.query(Model).filter(Model.ProjectId == projectid).all()
    else:
        models = session.query(Model).all()
    session.close()
    return models

def delete(modelId):
    session = database.get_session()
    session.query(Model).filter(Model.ModelId == modelId).delete()
    session.commit()
    session.close()