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
    email = Column("email", TEXT, nullable=False)

    def __init__(self, username, password, email):
            # id auto-increments
            self.username = username
            self.password = password
            self.email = email


class Post(Base):
    __tablename__ = "tweets"

    #columns
    id = Column("id", INTEGER, primary_key=True)
    word_count = Column("word_count", INTEGER)
    content = Column('content', TEXT)
    date = Column("date", TEXT)
    type = Column("type", TEXT)
    #user_id = relationship("") do this tomorrow

    
    def __init__(self, word_count, content, date, type):
            # id auto-increments
            self.content = content
            self.word_count = word_count
            self.date = date
            self.type = type