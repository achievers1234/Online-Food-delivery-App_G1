from flask import jsonify, Blueprint, request
from  backend.db import db
from backend.orders.order import Order
from flask_jwt_extended import jwt_required,get_jwt_identity

orders = Blueprint('orders', __name__, url_prefix='/orders')

#get all orders
@orders.route("/")
def all_orders():
    orders= Order.query.all()
    response = [{
        "quantity":item.quantity,
        "location":item.location,
        "order_status":item.order_status
        
    }for item in orders]
    return jsonify({
            "success":True,
            "data":response,
            "total":len(orders)
        }),200


# creating a new order 
@orders.route('/create', methods= ['POST'])
@jwt_required()
def creating_new_order():
    
    quantity = request.json['quantity']
    location = request.json['location']
    order_status = request.json['order_status']
    user_id = get_jwt_identity()
    food_item_id = request.json['food_item_id']
    
# adding validation on the order
    if not quantity: #if the order quantity is missing
        return jsonify({"message": "Your order quantity is required"}),400 
    
    # if the order entered exists
    existing_order = Order.query.filter_by(quantity=quantity).first()
    if existing_order is not None:
        return jsonify({"message": "order exists"}), 400
    
    if not location:
        return jsonify({"message": "delivery location is needed"}),400
    
    if order_status == True:
        return jsonify({"Message":"your order is being worked upon", "success": True}),200
    
    if order_status == False:
        return jsonify({"message": "order not made","suucess": False}),400
    
    if not user_id:
        return jsonify({"message": "User details are required"}),400
    
    if not food_item_id:
        return jsonify({"message": "Food details to be ordered are required"}),400
    
#creating an instance of a order
    new_order = Order(quantity=quantity,location=location,order_status=order_status,user_id=user_id, food_item_id=food_item_id)

# storing values
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "order made successfuly"}), 200

# getting an order
@orders.route ('/order/<int:id>', methods=['GET'])
def viewing_an_order(id):
    order = Order.query.get_or_404(id)

    response = {
            "id": order.id,
            "quantity":order.quantity,
            "location":order.location,
            "order_status": order.order_status
    }
    return jsonify({"message":"food item details retrieved", "order": response, "success": True}),200


# updating a order
@orders.route ('/order/<int:id>', methods=['PUT'])
def updating_order(id):
    order = Order.query.get_or_404(id)

    order.quantity = request.json['quantity']
    order.location = request.json['location']
    order.order_status = request.json['order_status']

    db.session.add(order)
    db.session.commit()
    return jsonify({"message":"order has been updated", "success": True}),200

# deleting a order
@orders.route('/order/<int:id>', methods=['DELETE'])
def deleting_order(id):
    order = Order.query.get_or_404(id)

    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "order has been deleted", "success":True}),200