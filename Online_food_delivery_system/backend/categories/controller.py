from flask import  jsonify, request, Blueprint
from backend.categories.category import Category
from backend.db import db
from flask_jwt_extended import get_jwt_identity,jwt_required
import datetime

categories = Blueprint('categories', __name__, url_prefix='/categories')

#get all categories
@categories.route('/')
def all_categories():
    categories= Category.query.all()
    response = [{
        "name":item.name,
        "image":item.image
    }for item in categories]
    return jsonify({
            "success":True,
            "data":response,
            "total":len(categories)
        }),200

# creating a new category 
@categories.route('/create', methods= ['POST'])
@jwt_required()
def creating_new_category():
    
    name = request.json['name']
    image = request.json['image']
    user_id=get_jwt_identity()
    
# adding validation on the category
    if not name: #if the category name is missing
        return jsonify({"message": "Your category name is required"}),400 
    
    # if the category entered exists
    existing_category = Category.query.filter_by(name=name).first()
    if existing_category is not None:
        return jsonify({"message": "category name already exists"}), 400
    
    
#creating an instance of a category
    new_category = Category(name=name, image=image,user_id=user_id)

# storing values
    db.session.add(new_category)
    db.session.commit()
    return jsonify({"message": "category added successfuly"}), 201

# getting a category
@categories.route ('/category/<int:id>', methods=['GET'])
def viewing_a_category(id):
    category = Category.query.get_or_404(id)

    response = {
            "id": category.id,
            "name":category.name,
    }
    return jsonify({"message":"category details retrieved", "category": response, "success": True}),200


# updating a category
@categories.route ('/category/<int:id>', methods=['PUT'])
def updating_category(id):
    category = Category.query.get_or_404(id)

    category.name = request.json['name']
    
    
    db.session.add(category)
    db.session.commit()
    return jsonify({"message":"category has been updated", "success": True}),200

# deleting a category
@categories.route('/category/<int:id>', methods=['DELETE'])
def deleting_category(id):
    category = Category.query.get_or_404(id)

    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "category has been deleted", "success":True}),200