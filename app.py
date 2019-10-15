
from flask import Flask,render_template,request,redirect,url_for,flash
# install Flask-SQLAlchemy (Armin Ronachoer)
from flask_sqlalchemy import SQLAlchemy
from configs.config import Development

app = Flask(__name__)
app.config.from_object(Development)
db = SQLAlchemy(app)

from models.inventory import InventoryModel


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def hello_world():
    return render_template('index.html')



@app.route('/inventory',methods=['GET','POST'])
def inventory():
    inve = InventoryModel.fetch_all()
    for each in inve:
        print(each)

    if request.method == 'POST':
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



if __name__ == '__main__':
    app.run(port=5005)
