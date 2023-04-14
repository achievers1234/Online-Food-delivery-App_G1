from backend.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Address(db.Model):
    __tablename__ = "addresses"
    
    name:str
    id:int
    district_id:int
    created_at:str
    updated_at:str
    

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),nullable=False)
    created_at = db.Column(db.String(255), default=datetime.now())
    updated_at = db.Column(db.String(255), onupdate=datetime.now())
    district_id = db.Column(db.Integer,db.ForeignKey('districts.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  

    def __init__(self, name,district_id, user_id): 
     self.district_id = district_id
     self.name = name
     self.user_id=user_id
    
     
    #  self.user_id=user_id
   
  

    def __repr__(self):
        return f"<Address {self.name} >"
