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

class PlainProjectSchema(Schema):
    id =fields.Int(dump_only=True)
    project_id = fields.Int(required=True)
    store_id = fields.Int(required=True)
    qr_id = fields.Int(required=True)
    hascode = fields.Str(required=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    price = fields.Str(required=True)
    material_list = fields.Str(required=True)
    project_link = fields.Str(required=True)
    status = fields.Str(required=True)

class StoreSchema(PlainStoreSchema):
    Material = fields.List(fields.Nested(PlainMaterialSchema()), dump_only=True)
    Products = fields.List(fields.Nested(PlainProductchema()), dump_only=True)

class ProjectSchema(PlainProjectSchema):
    Material = fields.List(fields.Nested(PlainMaterialSchema()), dump_only=True)
    Products = fields.List(fields.Nested(PlainProductchema()), dump_only=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True,load_only=True)