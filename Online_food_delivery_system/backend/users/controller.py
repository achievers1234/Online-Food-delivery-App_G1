from flask import jsonify, request, Blueprint
from backend.users.user import User
from backend.db import db
from werkzeug.security import generate_password_hash
import datetime

users = Blueprint('users', __name__, url_prefix='/users')

# getting all users
@users.route('/')
def all_users():
    users = User.query.all()
    return jsonify ({
        "success": True,
        "data": users,
        "total": len(users) #returns the total number of users
    }), 200





# creating a new user
@users.route('/create', methods= ['POST'])
def creating_user():
    
    name = request.json['name']
    contact = request.json['contact']
    email = request.json['email']
    password = request.json['password']
    # user_type =request.json['user_type']
    
    
# adding validation on the user
    if not name:
        return jsonify({"message": "Your name is required"}),400
    if not email:
        return jsonify({"message": "Your email is required"}),400
    if len(password)< 5:
        return jsonify ({"message": "Password must be greater than 5 characters"}),400
    
#creating an instance of a user
    new_user = User(name=name, contact=contact, email=email, password=password)

# creating a user and editing one
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 200


# getting a user
@users.route ('/user/<int:id>', methods=['GET'])
def viewing_user(id):
    user = User.query.get_or_404(id)

    response = {
            "id": user.id,
            "name":user.name,
            "contact": user.contact,
            "email": user.email,
            "password": user.password
        }
    return jsonify({"message":"User details retrieved", "user": response, "success": True}),200

# updating a user
@users.route ('/user/<int:id>', methods=['PUT'])
def updating_user(id):
    user = User.query.get_or_404(id)

    user.name = request.json['name']
    user.contact = request.json['contact']
    user.email = request.json['email']
    user.password = request.json['password']
    
    # inserting  the values 
    db.session.add(user)
    db.session.commit()
    return jsonify({"message":"User details updated", "success": True}),200

 # deleting a user 
@users.route ('/user/<int:id>', methods=['DELETE'])
def deleting_user(id):
    user = User.query.get_or_404(id)

# inserting values
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message":"User details deleted ", "success": True}),200
