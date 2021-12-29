delete_success = {
	"item_id" : 1
}

delete_error_1 = {
	"random" : 1
}

delete_error_2 = {
	"budget_id" : 1
}

delete_error_3 = {
	"item_id" : 1,
	"budget_id" : 1
}

put_success_1 = {
	"item_id" : 1
}

put_success_2 = {
	"item_id" : 1,
	"budget_id" : 1,
	"display_name" : "Some string",
	"value" : 100,
	"parent_id": 1
}

put_error_1 = {
	"budget_id" : 1,
	"display_name" : "Some string",
	"value" : 100,
	"parent_id": 1
}

put_error_2 = {
	"item_id" : 1,
	"random" : 1
}

post_success_1 = {
	"budget_id" : 1,
	"display_name" : "Some string",
	"value" : 100
}

post_success_2 = {
	"budget_id" : 1,
	"display_name" : "Some string",
	"value" : 100,
	"parent_id": 1
}

post_error_1 = {
	"budget_id" : 1,
	"display_name" : "Some string",
	"value" : 100,
	"parent_id": "String"
}

post_error_2 = {
	"display_name" : "Some string",
	"value" : 100
}

post_error_3 = {
	"budget_id" : 1,
	"display_name" : "Some string",
	"value" : 100,
	"random_value": 123
}