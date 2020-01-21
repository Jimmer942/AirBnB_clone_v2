#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")
