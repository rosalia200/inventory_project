from app import db
class InventoryModel(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    inventory_id = db.Column(db.Integer,nullable=False)
    quantity  = db.Column(db.Integer,nullable=False)
