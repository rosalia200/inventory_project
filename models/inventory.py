from app import db
class InventoryModel(db.Model):
    __tablename__ = "inventory"
    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40),nullable=False)
    type  = db.Column(db.String(40),nullable=False)
    buying_price = db.Column(db.Float,nullable=False)
    selling_price = db.Column(db.Float,nullable=False)
    stock = db.Column(db.Float,nullable=False)
    serial_number = db.Column(db.String(40),nullable=False,unique=True)

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_all(cls):
        return cls.query.all()