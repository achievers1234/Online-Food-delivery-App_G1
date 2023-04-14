from flask import Blueprint,request,jsonify
from backend.db import db
from backend.food_items.food_item import FoodItem
from flask_jwt_extended import jwt_required,get_jwt_identity
from backend.users.user import User

food_items = Blueprint('food_items',__name__,url_prefix='/food_items')



#get all food items
@food_items.route("/")
def all_food_items():

    user_id=get_jwt_identity()
    check_user_details=User.query.filter_by(id=user_id).first()
    user_type = check_user_details.user_type

    if user_type != "admin":
        return {'message':'It needs an admin'}
    
    else:


        food_items = FoodItem.query.all()

        response = [{
            "name":item.name,
            "image":item.image,
            "price":item.price
        }for item in food_items]


        return jsonify({"success":True,
                        "data":response,
                        "total":len(food_items)
                    }),200


# creating a new food_item 
@food_items.route('/create', methods= ['POST'])
@jwt_required()
def creating_new_food_item():

    user_id=get_jwt_identity()
    check_user_details=User.query.filter_by(id=user_id).first()
    user_type = check_user_details.user_type

    if user_type != "admin":
        return {'message':'It needs an admin'}
    
    else:
        
        name = request.json['name']
        price = request.json['price']
        image = request.json['image']
        user_id=get_jwt_identity()
        category_id = request.json['category_id']


    # adding validation on the food_item
        if not name: #if the food_item name is missing
            return jsonify({"message": "Your food_item name is required"}),400 
        
        # if the food_item entered exists
        existing_food_item = FoodItem.query.filter_by(name=name).first()
        if existing_food_item is not None:
            return jsonify({"message": "food item name already exists"}), 400
        
        
    #creating an instance of a food_item
        new_food_item = FoodItem(name=name,price=price,image=image,user_id=user_id,category_id=category_id)

    # storing values
        db.session.add(new_food_item)
        db.session.commit()
        return jsonify({"message": "food item added successfuly"}), 201

# getting a food_item
@food_items.route ('/food_item/<int:id>', methods=['GET'])
def viewing_a_food_item(id):

    user_id=get_jwt_identity()
    check_user_details=User.query.filter_by(id=user_id).first()
    user_type = check_user_details.user_type

    if user_type != "admin":
        return {'message':'It needs an admin'}
    
    else:
        food_item = FoodItem.query.get_or_404(id)

        response = {
                "id": food_item.id,
                "name":food_item.name,
                "price":food_item.price,
                "image": food_item.image
        }
        return jsonify({"message":"food item details retrieved", "food_item": response, "success": True}),200


# updating a food_item
@food_items.route ('/food_item/<int:id>', methods=['PUT'])
def updating_food_item(id):

    user_id=get_jwt_identity()
    check_user_details=User.query.filter_by(id=user_id).first()
    user_type = check_user_details.user_type

    if user_type != "admin":
        return {'message':'It needs an admin'}
    
    else:
    
    
        food_item = FoodItem.query.get_or_404(id)

        food_item.name = request.json['name']
        food_item.price = request.json['price']
        food_item.image = request.json['image']

        db.session.add(food_item)
        db.session.commit()
        return jsonify({"message":"food item has been updated", "success": True}),200

# deleting a food_item
@food_items.route('/food_item/<int:id>', methods=['DELETE'])
def deleting_food_item(id):

    user_id=get_jwt_identity()
    check_user_details=User.query.filter_by(id=user_id).first()
    user_type = check_user_details.user_type

    if user_type != "admin":
        return {'message':'It needs an admin'}
    
    else:
        food_item = FoodItem.query.get_or_404(id)

        db.session.delete(food_item)
        db.session.commit()
        return jsonify({"message": "food item has been deleted", "success":True}),200