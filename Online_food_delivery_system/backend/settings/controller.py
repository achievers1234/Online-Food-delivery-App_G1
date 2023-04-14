from flask import request, Blueprint,jsonify
from backend.settings.setting import Setting
from backend.db import db
import datetime
from flask_jwt_extended import jwt_required,get_jwt_identity
from backend.users.user import User


settings = Blueprint('settings', __name__, url_prefix='/settings')

@settings.route("/")
def all_settings():

    user_id=get_jwt_identity()
    check_user_details=User.query.filter_by(id=user_id).first()
    user_type = check_user_details.user_type

    if user_type != "admin":
        return {'message':'It needs an admin'}
    
    else:
        setting = Setting.query.all()
        return jsonify({
            "success": True,
            "data": setting,
            "total": len(setting)
        }),200


#creating a restaurant
@settings.route('/create', methods= ['POST'])
@jwt_required()
def creating_new_restaurant():

    user_id=get_jwt_identity()
    check_user_details=User.query.filter_by(id=user_id).first()
    user_type = check_user_details.user_type

    if user_type != "admin":
        return {'message':'It needs an admin'}
    

    else:

        data=request.get_json()

        name = data['name']
        email = data['email']
        contact = data['contact']
        location = data['location']
        user_id=get_jwt_identity()
        

    # adding validation on the settings of the restuarant
        if not name  : #if the restaurant is missing
            return jsonify({"message": "All fields are  required"}),400 
        
        # if the restaurant name entered exists
        existing_restaurant = Setting.query.filter_by(name=name).first()
        if existing_restaurant is not None:
            return jsonify({"message": "Restaurant name already exists"}), 400
        
        if not email:
            return jsonify({"message": "email is required"}),400
        
        existing_email = Setting.query.filter_by(email=email).first()
        if existing_email is not None:
            return jsonify({"message": 'email exists'}),400
        
        
    #creating an instance of a restaurant
        new_restaurant = Setting(name=name,email=email,contact=contact,location=location,user_id=user_id)
    # storing values
        db.session.add(new_restaurant)
        db.session.commit()
        return jsonify({"message": "restaurant added successfuly",
                        'data':new_restaurant}), 201


# updating a restaurant
@settings.route ('/setting/<int:id>', methods=['PUT'])
def updating_setting(id):

    user_id=get_jwt_identity()
    check_user_details=User.query.filter_by(id=user_id).first()
    user_type = check_user_details.user_type

    if user_type != "admin":
        return {'message':'It needs an admin'}
    

    else:

        setting = Setting.query.get_or_404(id)

        setting.name = request.json['name']
        
        db.session.add(setting)
        db.session.commit()
        return jsonify({"message":"Setting has been updated", "success": True}),200

    