from marshmallow import Schema, fields

class PostSchema(Schema):
	budget_id 		= fields.Integer(required=True)
	display_name 	= fields.String(required=True)
	value 			= fields.Number(required=True)
	parent_id		= fields.Integer(required=False)

class PutSchema(Schema):
	item_id 		= fields.Integer(required=True)
	budget_id 		= fields.Integer(required=False)
	display_name 	= fields.String(required=False)
	value 			= fields.Number(required=False)
	parent_id		= fields.Integer(required=False)

class DeleteSchema(Schema):
	item_id 		= fields.Integer(required=True)