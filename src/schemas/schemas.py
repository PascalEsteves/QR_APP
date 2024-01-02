from marshmallow import Schema, fields

class PlainMaterialSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainProductchema(Schema):
    id = fields.Int(dumpy_only=True)
    name = fields.Str(required=True)

class StoreSchema(PlainStoreSchema):
    Material = fields.List(fields.Nested(PlainMaterialSchema()), dump_only=True)
    Products = fields.List(fields.Nested(PlainProductchema()), dump_only=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True,load_only=True)