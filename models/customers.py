from main import db
from models.sales import SalesModel
class CustomersModel(db.Model):
    __tablename__ = "customers"
    id= db.Column(db.Integer,primary_key=True)
    customer_name = db.Column(db.String(40),nullable=False)
    gender = db.Column(db.String(40),nullable=False)
    national_id = db.Column(db.String(40),nullable=False,unique=True)
    contact  = db.Column(db.String(40),nullable=False,unique=True)
    email = db.Column(db.String(40),nullable=False,unique=True)
    inventories = db.relationship('InventoryModel', backref='customers', lazy=True)


    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()


    # @classmethod
    # def get_inventory_by_id(cls,id):
    #     return CustomersModel.query.filter_by(id=id).first()

    @classmethod
    def fetch_all(cls):
        return cls.query.all()

