from backend.db import db
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Region(db.Model):
    __tablename__ = "regions"

    
    name:str
    created_at:str
    updated_at:str
    created_by:int
    


    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    created_at = db.Column(db.String(255),nullable=True, default=datetime.now())
    updated_at = db.Column(db.String(255),nullable=True, onupdate=datetime.now())
    created_by  = db.Column(db.Integer,db.ForeignKey('users.id'))
    districts = db.relationship("District",backref="region")
   

    def __init__(self,name,created_by):
        self.name = name
        self.created_by = created_by
        

    def __repr__(self):
        return f"<Region {self.name} >"