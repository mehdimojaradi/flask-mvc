from flask import *
from flask_sqlalchemy import SQLAlchemy
from app.controllers import *
from json import JSONEncoder, JSONDecoder
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
    return redirect("/0")

@app.route('/<api>', methods=['GET'])
def list_employees(api):
    return EmployeesController.list_employees(api)

@app.route('/add', methods=['GET', 'POST'])
def add():
    return EmployeesController.add_employee()

@app.route('/test/<id>', methods=['GET', 'POST'])
def test(id):
    return JSONEncoder().encode({
        "msg": id
    })

if __name__ == '__main__':
    db.create_all()
    app.run("0.0.0.0", debug=True)
