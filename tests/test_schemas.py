from src.schemas import *
from marshmallow import ValidationError
import pytest
from tests.schema_samples import *

def test_post():
	schema = PostSchema()
	schema.load(post_success_1)
	schema.load(post_success_2)
	with pytest.raises(ValidationError) as e:
		schema.load(post_error_1)
	with pytest.raises(ValidationError) as e:
		schema.load(post_error_2)
	with pytest.raises(ValidationError) as e:
		schema.load(post_error_3)

def test_put():
	schema = PutSchema()
	schema.load(put_success_1)
	schema.load(put_success_2)
	with pytest.raises(ValidationError) as e:
		schema.load(put_error_1)
	with pytest.raises(ValidationError) as e:
		schema.load(put_error_2)

def test_delete():
	schema = DeleteSchema()
	schema.load(delete_success)
	with pytest.raises(ValidationError) as e:
		schema.load(delete_error_1)
	with pytest.raises(ValidationError) as e:
		schema.load(delete_error_2)
	with pytest.raises(ValidationError) as e:
		schema.load(delete_error_3)