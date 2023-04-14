from backend.db import db
from dataclasses import dataclass


# creating a class for the db
@dataclass
class Order(db.Model):
    __tablename__ = "orders"

    id=int
    quantity=int
    location=str
    order_status=str
    user_id=int
    food_item_id=int


    id = db.Column(db.Integer, primary_key = True)
    quantity = db.Column(db.Integer)
    location = db.Column(db.String(255),nullable=False)
    order_status=db.Column(db.String(255),default = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) #defining the relationship between the user and order
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_items.id')) #defining the relationship between the order and food items
   

# initialising the attributes of a class Order
    def __init__(self, quantity,location,order_status ,user_id,food_item_id):
        self.quantity = quantity
        self.location = location
        self.order_status=order_status
        self.user_id = user_id
        self.food_item_id = food_item_id

#  using a special method used to represent a class's objects as a string
    def __repr__(self):
        return f"<Order{self.user_id}>"
    
    