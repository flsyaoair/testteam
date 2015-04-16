# -*- coding: UTF-8 -*- 
from testTeam.models import case, database
from datetime import datetime

def create(case_name,description,versions,caseurl,creator):
    session = database.get_session()
    p = case()
    p.CaseName = case_name.stSrip()
    p.Creator = creator
    p.Description = description
    p.Versions = versions
    p.CaseURL = caseurl
    p.CreateDate = datetime.now()
    p.DownCount = 0
    session.add(p)
    session.commit()
    
def query_case(page_no,page_size,order_by,current_user,current_project):
    session = database.get_session()
    caseid_list = session.query(CaseId).filter(and_(Creator== current_user, ProjectId==current_project))
    case_list = session.query(CaseId,CaseName,Description,Versions,CaseURL).filter(case.CaseId.in_(caseid_list))
    (data,row_count,page_count,page_no) = database.query_more(case_list,order_by,page_no,page_size)
    
    session.close()
    return (data,row_count,page_count,page_no)

def del_case(Case_Id):    
    session = database.get_session()
    model = session.query(case).filter(case.CaseId == Case_Id).first()
    session.delete(model)
    session.commit()
    return True
    

def udpate_case(case_name,description,versions,Case_Id):
    session = database.get_session()
    case = session.query(case).filter(case.CaseId == Case_Id).first()
    case.CaseName = case_name
    case.Description = description
    case.Versions = versions
    session.commit()
    session.close()
    return True