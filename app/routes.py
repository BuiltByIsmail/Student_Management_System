from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Student
from werkzeug.security import generate_password_hash
from app import db

# ✅ Create Blueprint
main = Blueprint("main", __name__)

# -----------------------
# DASHBOARD ROUTE
# -----------------------
@main.route("/dashboard")
@login_required
def dashboard():
    return render_template("student_dashboard.html", student=current_user)


# -----------------------
# LANDING PAGE
# ----------------------- 
@main.route("/")
def home():
    return render_template("index.html")


# -----------------------
# LOGIN PAGE (VIEW ONLY)
# -----------------------
@main.route("/auth/login")
def login():
    return render_template("auth/login.html")


# -----------------------
# REGISTER PAGE (VIEW ONLY)
# -----------------------
@main.route("/auth/register")
def register():
    return render_template("auth/register.html")


# -----------------------
# CRUD: LIST STUDENTS
# -----------------------
@main.route("/students/list")
@login_required
def list_students():
    students = Student.query.all()
    return render_template("students/list.html", students=students)


# -----------------------
# CRUD: ADD STUDENT
# -----------------------

@main.route("/students/add", methods=["GET", "POST"])
@login_required
def add_student():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        matric_no = request.form.get("matric_no")
        department = request.form.get("department")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")  # <-- from form

        if not full_name or not matric_no or not department or not email or not password:
            flash("Please fill in all required fields!", "danger")
            return redirect(url_for("main.add_student"))

        # 👇 Hash password properly
        password_hash = generate_password_hash(password)

        new_student = Student(
            full_name=full_name,
            matric_no=matric_no,
            department=department,
            email=email,
            phone=phone,
            password_hash=password_hash
        )

        db.session.add(new_student)
        db.session.commit()

        flash("Student added successfully ✅", "success")
        return redirect(url_for("main.list_students"))

    return render_template("students/add.html")


# -----------------------
# CRUD: UPDATE STUDENT
# -----------------------
@main.route("/students/update/<int:student_id>", methods=["GET", "POST"])
@login_required
def update_student(student_id):
    student = Student.query.get_or_404(student_id)

    if request.method == "POST":
        student.full_name = request.form.get("full_name")
        student.matric_no = request.form.get("matric_no")
        student.department = request.form.get("department")
        student.email = request.form.get("email")
        student.phone = request.form.get("phone")

        db.session.commit()
        flash("Student updated successfully!", "success")
        return redirect(url_for("main.list_students"))

    return render_template("students/update.html", student=student)


# -----------------------
# CRUD: DELETE STUDENT
# -----------------------
@main.route("/students/delete/<int:student_id>", methods=["GET", "POST"])
@login_required
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)

    if request.method == "POST":
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for("main.list_students"))

    # GET request → show confirmation page with nice UI
    return render_template("students/delete.html", student=student)

