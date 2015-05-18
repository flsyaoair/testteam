# -*- coding: UTF-8 -*- 
from testTeam.models.database import BaseModel
from sqlalchemy import Column,DateTime,NVARCHAR,Integer,ForeignKey,UnicodeText
from sqlalchemy.orm import relationship
from testTeam.models.project import Project

class Model(BaseModel):
    __tablename__ = 'Model'
    ModelId = Column('ModelId', Integer,primary_key=True,nullable=False,autoincrement=True)
    ModelName = Column('ModelName', NVARCHAR(30),nullable=False)
    Description = Column('Description', UnicodeText)
    ProjectId = Column('ProjectId', Integer, ForeignKey('Project.ProjectId'))
    Project = relationship('Project', lazy='subquery', foreign_keys=ProjectId,primaryjoin=ProjectId == Project.ProjectId)
    Creator = Column('Creator', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    UserProfile = relationship("UserProfile")
    CreateDate = Column('CreateDate', DateTime,nullable=False)
    LastUpdateDate = Column('LastUpdateDate', DateTime,nullable=False)
    