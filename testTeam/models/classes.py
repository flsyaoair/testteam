# -*- coding: UTF-8 -*- 
from testTeam.models.database import BaseModel
from sqlalchemy import Column,DateTime,NVARCHAR,SMALLINT,Integer,ForeignKey,UnicodeText
from sqlalchemy.orm import relationship
from testTeam.models.project import Project

class Classes(BaseModel):
    
    __tablename__ = 'Classes'
    ClassId = Column('ClassId', Integer,primary_key=True,nullable=False,autoincrement=True)
    ClassName = Column('ClassName', NVARCHAR(30),nullable=False)
    ProjectId = Column('ProjectId', Integer, ForeignKey('Project.ProjectId'), nullable=False)
    Project = relationship('Project', foreign_keys=ProjectId,primaryjoin=ProjectId == Project.ProjectId)
    Creator = Column('Creator', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    UserProfile = relationship("UserProfile")
    CreateDate = Column('CreateDate', DateTime,nullable=False)
    LastUpdateDate = Column('LastUpdateDate', DateTime,nullable=False)