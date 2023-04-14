from flask import jsonify, request, Blueprint
from backend.regions.region import Region
from backend.db import db
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.users.user import User

regions = Blueprint("regions", __name__, url_prefix="/regions")

# getting all regions 
@regions.route("/")
def all_regions():

    user_id=get_jwt_identity()
    check_user_details=User.query.filter_by(id=user_id).first()
    user_type = check_user_details.user_type

    if user_type != "admin":
        return {'message':'It needs an admin'}
    
    else:
        regions = Region.query.all()
        return jsonify ({
            "success":True,
            "data": regions,
            "total": len(regions)
        }), 200


# creating a new region 
@regions.route('/create', methods= ['POST'])
@jwt_required()
def creating_new_region():

    user_id=get_jwt_identity()
    check_user_details=User.query.filter_by(id=user_id).first()
    user_type = check_user_details.user_type

    if user_type != "admin":
        return {'message':'It needs an admin'}
    
    else:
    
        name = request.json['name']
        created_by=get_jwt_identity()
        # created_by = request.json['created_by']

        
        
    # adding validation on the region
        if not name: #if the region name is missing
            return jsonify({"message": "Your region name is required"}),400 
        
        # if the region entered exists
        existing_region = Region.query.filter_by(name=name).first()
        if existing_region is not None:
            return jsonify({"message": "Region name already exists"}), 400
        
        
    #creating an instance of a region
        new_region = Region(name=name,created_by=created_by)

    # storing values
        db.session.add(new_region)
        db.session.commit()
        return jsonify({"message": "Region added successfuly"}), 201

# getting a region
@regions.route ('/region/<int:id>', methods=['GET'])
def viewing_a_region(id):

    user_id=get_jwt_identity()
    check_user_details=User.query.filter_by(id=user_id).first()
    user_type = check_user_details.user_type

    if user_type != "admin":
        return {'message':'It needs an admin'}
    
    else:
        region = Region.query.get_or_404(id)

        response = {
                "id": region.id,
                "name":region.name,
        }
        return jsonify({"message":"Region details retrieved", "region": response, "success": True}),200


# updating a region
@regions.route ('/region/<int:id>', methods=['PUT'])
def updating_region(id):

    user_id=get_jwt_identity()
    check_user_details=User.query.filter_by(id=user_id).first()
    user_type = check_user_details.user_type

    if user_type != "admin":
        return {'message':'It needs an admin'}
    
    else:
        region = Region.query.get_or_404(id)

        region.name = request.json['name']
        region.updated_at=datetime.now()
        
        db.session.add(region)
        db.session.commit()
        return jsonify({"message":"Region has been updated", "success": True}),200

# deleting a region
@regions.route('/region/<int:id>', methods=['DELETE'])
def deleting_region(id):

    user_id=get_jwt_identity()
    check_user_details=User.query.filter_by(id=user_id).first()
    user_type = check_user_details.user_type

    if user_type != "admin":
        return {'message':'It needs an admin'}
    
    else:

        region = Region.query.get_or_404(id)

        db.session.delete(region)
        db.session.commit()
        return jsonify({"message": "Region has been deleted", "success":True}),200