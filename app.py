from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Float

app = Flask(__name__)
app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>Welcome to My Flask App</h1><p>This is a simple web page.</p>"
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# db = SQLAlchemy(app)

# Employee Model
# class Employee(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(100), nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)
    # department = db.Column(db.String(50))
    # salary = db.Column(db.Float)

class Base(DeclarativeBase):
    pass

# SQLAlchemy init
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Employee Model using New Style
class Employee(db.Model):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    department: Mapped[str] = mapped_column(String(50), default="General")
    salary: Mapped[float] = mapped_column(Float, default=0.0)

# Create DB
with app.app_context():
    db.create_all()

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_emp = Employee(
        
        name=data['name'],
        email=data['email'],
        department=data.get('department', 'General'),
        salary=data.get('salary', 0.0)
    )
    db.session.add(new_emp)
    db.session.commit()
    return jsonify({"message": "Employee added successfully!"})

@app.route('/employees', methods=['GET'])
def get_employees():
    employees=db.session.query(Employee).all()
    result = [
        {
            "id": emp.id,
            "name": emp.name,
            "email": emp.email,
            "department": emp.department,
            "salary": emp.salary,
        }
        for emp in employees
    ]
    
    return jsonify(result)



@app.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):
    emp = db.session.get(Employee, id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json()
    emp.name = data.get("name", emp.name)
    emp.email = data.get("email", emp.email)
    emp.department = data.get("department", emp.department)
    emp.salary = data.get("salary", emp.salary)

    db.session.commit()
    return jsonify({"message": "Employee updated successfully!"})

@app.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    emp = db.session.get(Employee, id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    db.session.delete(emp)
    db.session.commit()
    return jsonify({"message": "Employee deleted successfully!"})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
