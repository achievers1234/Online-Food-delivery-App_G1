from backend.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User(db.Model):
    __tablename__ = 'users'

    name:str
    email:str
    contact:str
    id:int
    user_type:str

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    contact =db.Column(db.String(150))
    user_type = db.Column(db.String(150) ,default="Client")
    password = db.Column(db.String(50))
    created_at = db.Column(db.String(150), default=datetime.now())
    updated_at = db.Column(db.String(150), onupdate=datetime.now())
    addresses = db.relationship("Address", backref="user")
    orders = db.relationship("Order", backref='user')
    regions = db.relationship("Region", backref='user')


    def __init__(self, name, email, contact, password):
        self.name = name
        self.email = email 
        self.contact = contact 
        self.password = password 
        # self.user_type=user_type
        # self.created_at = created_at
        # self.updated_at = updated_at

    def __repr__(self):
        return f"<User {self.name}>"
    
    #saving a new instance
    def save(self):
        db.session.add(self)
        db.session.commit()

   #deleting an instance
    def delete(self):
        db.session.delete(self)
        db.session.commit()