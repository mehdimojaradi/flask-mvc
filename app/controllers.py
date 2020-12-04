from flask import *
from app.models import *
from json import JSONEncoder, JSONDecoder

class EmployeesController:

    def list_employees(api):
        employees = Employees.query.all()
        row = []
        for employee in employees:
            row.append({
                'name': employee.name, 
                'salary':employee.salary,
                'age':employee.age,
                'pin':employee.pin,
            })
        if api is "0":
            return render_template("list_employees.html", employees=employees)
        if api is "1":
            return JSONEncoder().encode({ "employee" : row })
        else:
            raise ValueError

    def add_employee():
        if request.method == 'POST':
            if not request.form['name'] or not request.form['salary'] or not request.form['age']:
                flash('Please enter all the fields', 'error')
            else:
                employee = Employees(
                    request.form['name'],
                    request.form['salary'],
                    request.form['age'],
                    request.form['pin']
                )

                db.session.add(employee)
                db.session.commit()
                flash('Record was successfully added')

                return redirect(url_for('index'))
        return render_template('add.html')
