# Student Information System (Flask) - Boilerplate

## Setup
1. python -m venv venv
2. source venv/bin/activate   # or venv\Scripts\activate on Windows
3. pip install -r requirements.txt
4. flask db init
5. flask db migrate -m "initial"
6. flask db upgrade
7. flask run

Default DB: instance/site.db
## DB setup
flask shell
# create tables id starting fresh
1. from app import db
2. db.create_all()

# Drop Database table
1. from app import db
2. db.drop_all

# Add student
1. from app.models import Student
2. from app import db

s = Student(
    full_name="",
    matric_n0="",
    department="",
    email="",
    phone"",
)
s.set_password("secret1234")  # Always use hashed password
db.session.add(s)
db.session.commit()

# Query Student

# Get all
students = Student.query.all()

# Get first 
s = Student.query.first()

# Get by matric no
Student.query.filter_by(matric_no"").first()
print(s.full_name, s.email)

# Update 
s = Student.query.filter_by(matric_no="").first()
s.phone = ""
db.session.commit()

# Delate
s = Student.query.filter_by(matric_no="").first()
db.session.delete(s)
db.session.commit()

# Debug Command
from app.models import Student

# See all students
for s in Student.query.all():
    print(s.id, s.full_name, s.matric_no, s.email)

# Show password hash
print(s.password_hash)


