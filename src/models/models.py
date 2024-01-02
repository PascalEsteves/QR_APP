from src.models.database import db

class QR_Model(db.Model):
    __tablename__ = 'QR_Table'

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String, unique=True, nullable = False)
    code = db.Column(db.String, nullable=False)
    path = db.Column(db.String, unique= True, nullable = False)

class MaterialModel(db.Model):
    __tablename__ = "Material_Table"

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String, unique=True, nullable = False)
    code = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable = False)

class ProductModel(db.Model):
    __tablename__ = "Products_Table"

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String, nullable = False)
    code = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable = False)
    info = db.Column(db.String, nullable = False)
    quantity = db.Column(db.String, nullable = False)

class StoreModel(db.Model):
    __tablename__ = "Store_Table"

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String, nullable=False)
    products = db.Column()

    