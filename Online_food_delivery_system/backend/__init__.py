from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from backend.db import db
from flask_cors import CORS
from flasgger import Swagger, swag_from #for app to read swagg and create yaml files for desribing specs
from srcapi.config.swagger import template, swagger_config


def create_app(config_name):
    app= Flask(__name__)
    app.config.from_object(config[config_name])
    app.config.from_pyfile("../config.py")

    db.init_app(app)
    CORS(app)
    

    # importing the blueprints
    from backend.users.controller import  users
    from backend.addresses.controller import addresses
    from backend.categories.controller import categories
    from backend.districts.controller import districts
    from backend.food_items.controller import food_items
    from backend.orders.controller import orders
    from backend.settings.controller import settings
    from backend.regions.controller import regions
    from backend.auth.controller import auth
    # registering the blueprints
    app.register_blueprint(users)
    app.register_blueprint(food_items)
    app.register_blueprint(orders)
    app.register_blueprint(categories)
    app.register_blueprint(addresses)
    app.register_blueprint(districts)
    app.register_blueprint(settings)
    app.register_blueprint(regions)
    app.register_blueprint(auth)

    Swagger(app, config=swagger_config, template=template)

    
    return app