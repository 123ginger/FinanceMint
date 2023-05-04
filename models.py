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
    username = Column("username", TEXT, primary_key=True)
    password = Column("password", TEXT, nullable=False)

    def __init__(self, username, password):
            # id auto-increments
            self.username = username
            self.password = password


class Post(Base):
    __tablename__ = "posts"

    #columns
    id = Column("id", INTEGER, primary_key=True)
    content = Column('content', TEXT)
    date = Column("date", TEXT)
    type = Column("type", TEXT)
    #user_id = relationship("") do this tomorrow

    
    def __init__(self, content, date, type):
            # id auto-increments
            self.content = content
            self.date = date
            self.type = type