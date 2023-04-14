from backend.db import db
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Setting(db.Model):
    __tablename__ = 'settings'

    id=int
    name=str
    email=str
    contact=str
    location=str
    working_time=str

    
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    contact = db.Column(db.String(200))
    location = db.Column(db.String(200))
    working_time = db.Column(db.String(200),default=datetime.now())
    user_id =db.Column(db.Integer)


    def __init__(self, name,email,contact,location,user_id):
        
        self.name = name
        self.email = email
        self.contact = contact
        self.location = location
        self.user_id = user_id
        # self.working_time=working_time

    def __repr__(self):
        return f"<Setting {self.name}>"