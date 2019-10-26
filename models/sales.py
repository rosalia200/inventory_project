from main import db
class SalesModel(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    # inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    # inventory_id = db.Column(db.Integer,nullable=False)f
    quantity  = db.Column(db.Integer,nullable=False)




    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    # @classmethod
    # def fetch_all(cls):
    #     return cls.query.all()
