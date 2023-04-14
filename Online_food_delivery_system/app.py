from flask import Flask
from backend import create_app
from backend.db import db
from flask_migrate import Migrate
from backend.users.user import User
from backend.food_items.food_item import FoodItem
from backend.districts.district import District
from backend.categories.category import Category
from backend.regions.region import Region
from backend.settings.setting import Setting
from backend.addresses.address import Address
from backend.orders.order import Order
from flask_jwt_extended import JWTManager

app = create_app('development')
migrate = Migrate(app, db)
jwt = JWTManager(app)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User, FoodItem=FoodItem, District=District, Category=Category, Region=Region,Order=Order, Address=Address, Setting=Setting)