from backend.db import db
from dataclasses import dataclass
from datetime import datetime


@dataclass
class FoodItem(db.Model):
  __tablename__ = 'food_items'

  id=int
  name=str
  price=str
  image=str
  stock=int
  user_id=int
  price_unit=str
  category_id=int
  created_at=str
  updated_at=str

  
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100),unique=True)
  price = db.Column(db.String(255))  
  price_unit = db.Column(db.String(10),default='ugx')
  image = db.Column(db.String(200))
  stock = db.Column(db.Integer)
  created_at = db.Column(db.String(255),nullable=True, default=datetime.now())
  updated_at = db.Column(db.String(255),nullable=True, onupdate=datetime.now())
  user_id  = db.Column(db.Integer,db.ForeignKey('users.id'))
  category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
  
  


  def __init__(self, name,image,price,category_id,user_id):
   self.name = name
   self.image = image
   self.price = price
  #  self.price_unit = price_unit
   self.category_id = category_id
  #  self.stock = stock
   self.user_id = user_id
  #  self.created_at = created_at
  #  self.updated_at =updated_at

  

  def __repr__(self):
        return f"<FoodItem {self.name} >"
  

        