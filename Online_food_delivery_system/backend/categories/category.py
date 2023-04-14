from backend.db import db
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Category(db.Model):
    __tablename__ = "categories"

    id=int
    name=str
    image=str

    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    image = db.Column(db.String(255),nullable=False)
    created_at = db.Column(db.String(255),nullable=True, default=datetime.now())
    updated_at = db.Column(db.String(255),nullable=True,onupdate=datetime.now())
    user_id  = db.Column(db.Integer,db.ForeignKey('users.id'))
    
   

    def __init__(self, image, name,user_id):
     self.image = image
     self.name = name
     self.user_id = user_id
    #  self.created_at = created_at
    #  self.updated_at = updated_at
    

    def __repr__(self):
        return f"<Category {self.name} >"