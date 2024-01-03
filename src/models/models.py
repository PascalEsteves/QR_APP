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
    store_id = db.Column(db.Integer, db.ForeignKey("Store_Table.id"))
    qr_id = db.Column(db.Integer, db.ForeignKey('QR_Table.id'))
    code = db.Column(db.String, unique=True,nullable=False)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    price = db.Column(db.String, nullable = False)

class StockModel(db.Model):
    __tablename__ = "Stock_Table"

    id = db.Column(db.Integer, primary_key = True)
    store_id = db.Column(db.Integer, db.ForeignKey("Store_Table.id"))
    material_code = db.Column(db.String, db.ForeignKey("Material_Table.code"))
    quantity = db.Column(db.Float, nullable = False)

class ProjectModel(db.Model):
    __tablename__ = "Project_Table"

    id = db.Column(db.Integer, primary_key =True)
    store_id = db.Column(db.Integer, db.ForeignKey("Store_Table.id"))
    qr_id = db.Column(db.Integer, db.ForeignKey('QR_Table.id'))
    hascode = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable = False)
    location = db.Column(db.String, nullable = False)
    price = db.Column(db.Float, nullable = False)
    material_list =db.Column(db.String, nullable=False)
    project_link = db.Column(db.String, nullable = False)
    status = db.Column(db.String, nullable = False)

class StoreModel(db.Model):
    __tablename__ = "Store_Table"

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String, nullable=False)