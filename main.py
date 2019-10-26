
from flask import Flask,render_template,request,redirect,url_for,flash
# install Flask-SQLAlchemy (Armin Ronachoer)
from flask_sqlalchemy import SQLAlchemy
from configs.config import Production

app = Flask(__name__)
app.config.from_object(Production)
db = SQLAlchemy(app)

from models.inventory import InventoryModel
from models.sales import SalesModel
from models.customers import CustomersModel


@app.before_first_request
def create_tables():
    db.create_all()


# @app.route('/')
# def hello_world():
#     customers = CustomersModel.fetch_all()
#     return render_template('index.html',customers=customers)
@app.route('/')
def hello_world():
    return render_template('index.html')
#
# @app.route('/newCustomer',methods=['POST'])
# def newCustomer():
#     customer_name= request.form['name']
#     gender = request.form['gender']
#     email = request.form['email']
#     contact = request.form['contact']
#
#     national_id = request.form['national_id']
#     emp = CustomersModel(customer_name=customer_name,gender=gender,contact=contact,email=email,national_id=national_id)
#
#
#     emp.insert_to_db()
#     return redirect(url_for('hello_world'))


@app.route('/inventory')
def inventory():
    inve = InventoryModel.fetch_all()
    for each in inve:
        print(each.name)
    return render_template('inventory.html',inventory=inve)

@app.route('/sales')
def sales():
    return render_template('sales.html')


@app.route('/inventory/<int:id>/sales', methods=['GET'])
def view_sales(id):

    # inventories = InventoryModel.fetch_all()
    this_inventory = InventoryModel.get_inventory_by_id(id)
    sales = this_inventory.sales
    return render_template('view_sales.html',sales=sales)
    # # return redirect(url_for('sales'))



@app.route('/addInventory',methods=['POST'])
def addInventory():

    name = request.form['name']
    type = request.form['type']
    buying_price = request.form['bp']
    selling_price = request.form['sp']
    stock = request.form['stock']
    serial_number = request.form['sn']

        # print(name)
        # print(type)
        # print(buying_price)
        # print(selling_price)
        # print(stock)
        # print(serial_number)
    inv =InventoryModel(name=name,type=type,buying_price=buying_price,selling_price=selling_price,stock=stock,serial_number=serial_number)
    inv.insert_to_db()
    return render_template('inventory.html')


@app.route('/addSales',methods=['POST'])
def addSales():

    inventory_id = request.form['inventory_id']
    quantity = request.form['quantity']

    sles =SalesModel(inventory_id=inventory_id,quantity=quantity)
    sles.insert_to_db()
    return render_template('sales.html')


if __name__ == '__main__':
    app.run(port=5005,debug=True)
