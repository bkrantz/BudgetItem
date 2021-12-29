from src.schemas import *
from src.app import app, db
from src.models import BudgetItem
from flask import request, jsonify
from marshmallow import ValidationError

NO_CONTENT_RESPONSE = {"budget_items": []}

# GET by item_id
@app.route('/budget_items/by_item/<int:item_id>', methods=['GET'])
def get_budget_item_by_item(item_id):
	budget_items = BudgetItem.query.filter_by(item_id=item_id).all()
	if len(budget_items) == 0:
		return NO_CONTENT_RESPONSE, 204
	return {"budget_items": [b.to_json() for b in budget_items]}, 200

# GET by budget_id
@app.route('/budget_items/by_budget/<int:budget_id>', methods=['GET'])
def get_budget_item_by_budget(budget_id):
	budget_items = BudgetItem.query.filter_by(budget_id=budget_id).all()
	if len(budget_items) == 0:
		return NO_CONTENT_RESPONSE, 204
	return {"budget_items": [b.to_json() for b in budget_items]}, 200

# GET all
@app.route('/budget_items', methods=['GET'])
def get_budget_items():
	budget_items = BudgetItem.query.filter_by().all()
	if len(budget_items) == 0:
		return NO_CONTENT_RESPONSE, 204
	return {"budget_items": [b.to_json() for b in budget_items]}, 200

# POST single new budget_item
@app.route('/budget_items', methods=['POST'])
def create_budget_item():
	request_body = request.json
	schema = PostSchema()
	try:
		result = schema.load(request_body)
	except ValidationError as err:
		return jsonify({"error": err.messages}), 400
	item = BudgetItem(**result)
	db.session.add(item)
	db.session.commit()
	budget_item = BudgetItem.query.filter_by(item_id=item.item_id).first()
	return {"budget_items": [budget_item.to_json()]}, 201

# DELETE single existing budget_item
@app.route('/budget_items', methods=['DELETE'])
def remove_budget_item():
	request_body = request.json
	schema = DeleteSchema()
	try:
		result = schema.load(request_body)
	except ValidationError as err:
		return jsonify({"error": err.messages}), 400
	item_id = request_body.get("item_id")
	budget_items = BudgetItem.query.filter_by(item_id=item_id).all()
	if len(budget_items) == 0:
		return NO_CONTENT_RESPONSE, 204
	db.session.delete(budget_items[0])
	db.session.commit()
	return {"budget_items": [budget_items[0].to_json()]}, 200

# PUT single update to existing budget_item
@app.route('/budget_items', methods=['PUT'])
def update_budget_item():
	request_body = request.json
	schema = PutSchema()
	try:
		result = schema.load(request_body)
	except ValidationError as err:
		return jsonify({"error": err.messages}), 400
	item_id = request_body.get("item_id")
	budget_item = BudgetItem.query.filter_by(item_id=item_id).first()
	if budget_item is None:
		return NO_CONTENT_RESPONSE, 204
	for field, new_value in request_body.items():
		if field != "item_id":
			setattr(budget_item, field, new_value)
	db.session.commit()
	return {"budget_items": [budget_item.to_json()]}, 200
