from flask import  jsonify, request, Blueprint
from backend.districts.district import District
from backend.db import db
from datetime import datetime
from flask_jwt_extended import jwt_required,get_jwt_identity

districts = Blueprint('districts', __name__, url_prefix='/districts')

#get all districts
@districts.route("/")
def all_districts():
    districts= District.query.all()
    return jsonify({
            "success":True,
            "data":districts,
            "total":len(districts)
        }),200


# creating a new district
@districts.route('/create', methods= ['POST'])
@jwt_required()
def creating_new_district():
    
    name = request.json['name']
    region_id = request.json['region_id']
    created_by = get_jwt_identity()
    
    
# adding validation on the district
    if not name: #if the district name is missing
        return jsonify({"message": "Your district name is required"}),400 
    
    # if the district entered exists
    existing_district = District.query.filter_by(name=name).first()
    if existing_district is not None:
        return jsonify({"message": "district name already exists"}), 400
    
    
#creating an instance of a district
    new_district = District(name=name,region_id=region_id,created_by=created_by,created_at=datetime.now(),updated_at=datetime.now())

# storing values
    db.session.add(new_district)
    db.session.commit()
    return jsonify({"message": "district added successfuly"}), 201


# getting a district
@districts.route ('/district/<int:id>', methods=['GET'])
def viewing_a_district(id):
    district = District.query.get_or_404(id)

    response = {
            "id": district.id,
            "name":district.name,
    }
    return jsonify({"message":"district details retrieved", "district": response, "success": True}),200


# updating a district
@districts.route ('/district/<int:id>', methods=['PUT'])
def updating_district(id):
    district = District.query.get_or_404(id)


    district.name = request.json['name']
    district.updated_at=datetime.now()
    
    db.session.add(district)
    db.session.commit()
    return jsonify({"message":"District has been updated", "success": True}),200


# deleting a district
@districts.route('/district/<int:id>', methods=['DELETE'])
def deleting_district(id):
    district = District.query.get_or_404(id)

    db.session.delete(district)
    db.session.commit()
    return jsonify({"message": "district has been deleted", "success":True}),200