from main import db

class Employees(db.Model):
    id = db.Column('employee_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    salary = db.Column(db.Float(50))
    age = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, salary, age, pin):
        self.name = name
        self.salary = salary
        self.age = age
        self.pin = pin
