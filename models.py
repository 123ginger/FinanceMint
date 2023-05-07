"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT, DATETIME
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    # Columns
    id = Column("id", INTEGER, primary_key=True, autoincrement=True)
    username = Column("username", TEXT, nullable=False)
    password = Column("password", TEXT, nullable=False)
    posts = relationship("Post", back_populates="user")

    def __init__(self, username, password):
            # id auto-increments
            self.username = username
            self.password = password


class Post(Base):
    __tablename__ = "posts"

    #columns
    id = Column("id", INTEGER, primary_key=True, autoincrement=True)
    content = Column('content', TEXT)
    date = Column("date", TEXT)
    type = Column("type", TEXT)
    user_id = Column(INTEGER, ForeignKey('users.id'))
    user = relationship("User", back_populates="posts")

    
    def __init__(self, content, date, type):
            # id auto-increments
            self.content = content
            self.date = date
            self.type = type