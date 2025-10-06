from .extensions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# ✅ Students are the only users in the system
class Student(db.Model, UserMixin):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    matric_no = db.Column(db.String(50), unique=True, nullable=False)
    department = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)

    password_hash = db.Column(db.String(200), nullable=False)

    courses = db.relationship("Course", backref="student", lazy=True)
    payments = db.relationship("Payment", backref="student", lazy=True)
    results = db.relationship("Result", backref="student", lazy=True)


    def __repr__(self):
        return f"<Student {self.full_name} - {self.matric_no} >"
 
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(int(user_id))
    
    

# ✅ Courses
class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(20), nullable=False)
    course_name = db.Column(db.String(120), nullable=False)
    credit_unit = db.Column(db.Integer, nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)


# ✅ Payments
class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Pending")

    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)


# ✅ Results
class Result(db.Model):
    __tablename__ = "results"

    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(20), nullable=False)
    grade = db.Column(db.String(2), nullable=False)
    semester = db.Column(db.String(20), nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)

