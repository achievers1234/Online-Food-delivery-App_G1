from flask import  jsonify, request, Blueprint
from backend.addresses.address import Address
from backend.db import db
from datetime import datetime
from flask_jwt_extended import jwt_required,get_jwt_identity

addresses = Blueprint('addresses', __name__, url_prefix='/addresses')

#get all addresses
@addresses.route("/")
def all_addresses():
    addresses= Address.query.all()
    return jsonify({
            "success":True,
            "data":addresses,
            "total":len(addresses)
        }),200

# creating a new address 
@addresses.route('/create', methods= ['POST'])
@jwt_required()
def creating_new_address():
    data=request.get_json()

    name = data['name']
    district_id = data['district_id']
    user_id = get_jwt_identity()
    
    
    
        
# adding validation on the address
    if not name or not district_id : #if the address name and district is missing
        return jsonify({"message": "All fields are  required"}),400 
    
    # if the address entered exists
    existing_address = Address.query.filter_by(name=name).first()
    if existing_address is not None:
        return jsonify({"message": "Address name already exists"}), 400
    
     #check for an address with same district
    if Address.query.filter_by(district_id=district_id).first():
        return jsonify({'error': "Address with this district name exists"}), 400 

    
    
#creating an instance of a address
    new_address = Address(name=name,district_id=district_id,user_id=user_id)
# storing values
    db.session.add(new_address)
    db.session.commit()
    return jsonify({"message": "address added successfuly",
                    'data':new_address}), 201

# getting a address
@addresses.route ('/address/<int:id>', methods=['GET'])
def viewing_an_address(id):
    address = Address.query.get_or_404(id)

    response = {
            "id": address.id,
            "name":address.name,
            "district_id":address.district_id,
            "user_id":address.user_id
    }
    return jsonify({"message":"address details retrieved", "address": response, "success": True}),200


# updating an address
@addresses.route ('/address/<int:id>', methods=['PUT'])
def updating_address(id):
    address = Address.query.get_or_404(id)

    address.name = request.json['name']
    address.updated_at=datetime.now()
    
    db.session.add(address)
    db.session.commit()
    return jsonify({"message":"address has been updated", "success": True}),200

# deleting a address
@addresses.route('/address/<int:id>', methods=['DELETE'])
def deleting_address(id):
    address = Address.query.get_or_404(id)

    db.session.delete(address)
    db.session.commit()
    return jsonify({"message": "address has been deleted", "success":True}),200