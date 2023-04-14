from backend.db import db
from dataclasses import dataclass
from datetime import datetime


@dataclass
class District(db.Model):
    __tablename__ = "districts"
    id:int
    name:str
    region_id:int


    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    created_at = db.Column(db.String(255),nullable=True,default=datetime.now())
    updated_at = db.Column(db.String(255),nullable=True, onupdate=datetime.now())
    region_id = db.Column(db.Integer,db.ForeignKey('regions.id'))
    created_by  = db.Column(db.Integer,db.ForeignKey('users.id'))
    addresses = db.relationship("Address",backref="district")
   

    def __init__(self, name,created_by,region_id,created_at,updated_at):
        
        self.name = name
        self.created_by = created_by
        self.region_id = region_id
        self.created_at = created_at
        self.updated_at = updated_at
    

    def __repr__(self):
        return f"<District {self.name} >"