from main import db
from models.sales import SalesModel
class InventoryModel(db.Model):
    __tablename__ = "inventory"
    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40),nullable=False)
    type  = db.Column(db.String(40),nullable=False)
    buying_price = db.Column(db.Float,nullable=False)
    selling_price = db.Column(db.Float,nullable=False)
    stock = db.Column(db.Float,nullable=False)
    serial_number = db.Column(db.String(40),nullable=False)
    #sales = db.relationship('SalesModel',backref=db.backref('posts', lazy=True))
    sales = db.relationship('SalesModel', backref='inventory', lazy=True)
    # customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_all(cls):
        return cls.query.all()
    @classmethod
    def get_inventory_by_id(cls,id):
        return InventoryModel.query.filter_by(id=id).first()
