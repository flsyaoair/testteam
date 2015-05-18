# -*- coding: UTF-8 -*- 

from testTeam.models.database import BaseModel
from testTeam.models.userprofile import UserProfile
from testTeam.models.project import Project
from sqlalchemy import Column,ForeignKey, Integer
from sqlalchemy.orm import relationship

class Member(BaseModel):

    __tablename__ = 'Member'
    MemberId = Column('MemberId', Integer,primary_key=True,nullable=False,autoincrement=True)
    ProjectId = Column('ProjectId', Integer,ForeignKey('Project.ProjectId'),nullable = False)
    Project = relationship('Project', foreign_keys=ProjectId,primaryjoin=ProjectId == Project.ProjectId)
    UserId = Column('UserId', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    User = relationship('UserProfile',lazy='subquery', foreign_keys=UserId,primaryjoin=UserId == UserProfile.UserId)