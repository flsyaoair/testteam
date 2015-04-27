# -*- coding: UTF-8 -*- 
from testTeam.models.database import BaseModel
from testTeam.models.userprofile import UserProfile
from testTeam.models.project import Project
from sqlalchemy import Column,DateTime,NVARCHAR,Integer,ForeignKey,UnicodeText

class case(BaseModel):   
    __tablename__ = 'case'
    CaseId = Column('CaseId', Integer,primary_key=True,nullable=False,autoincrement=True)
    CaseName = Column('CaseName', NVARCHAR(30),nullable=False)    
    ProjectId = Column('ProjectId', Integer,ForeignKey('Project.ProjectId'),nullable = False) 
    Creator = Column('Creator', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    Description = Column('Description', UnicodeText)
    Versions = Column("Versions", NVARCHAR(10),nullable=False)
    CaseURL = Column('CaseURL', NVARCHAR(100),nullable=False)
    CreateDate = Column('CreateDate', DateTime,nullable=False)
    LastUpdateDate = Column('LastUpdateDate', DateTime,nullable=False)    
    DownCount = Column('DownCount', Integer, nullable=True)