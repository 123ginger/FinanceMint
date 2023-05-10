"""
A fully functioning website that is aimed to address the economic difficulties 
that come with living in the bay area.

Created by: Bradford Tudor 
Date: May 2023
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT, DATETIME
from sqlalchemy.orm import relationship
from database import Base

# User class
class User(Base):
    __tablename__ = "users"

    username = Column("username", TEXT, primary_key=True, nullable=False)
    password = Column("password", TEXT, nullable=False)
    # Here I am showing an understanding of relationships
    posts = relationship("Post", back_populates="user")

    def __init__(self, username, password):
            # id auto-increments
            self.username = username
            self.password = password


# Post class
class Post(Base):
    __tablename__ = "posts"

    id = Column("id", INTEGER, primary_key=True, autoincrement=True)
    content = Column('content', TEXT)
    date = Column("date", TEXT)
    type = Column("type", TEXT)
    # Here I am showing an understanding of relationships
    user_id = Column(TEXT, ForeignKey('users.username'))
    user = relationship("User", back_populates="posts")
    
    def __init__(self, content, date, type, user_id):
            # id auto-increments
            self.content = content
            self.date = date
            self.type = type
            self.user_id = user_id