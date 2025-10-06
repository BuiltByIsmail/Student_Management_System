from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from app.models import Student
from app import db
from werkzeug.security import check_password_hash

auth = Blueprint("auth", __name__)

# -----------------------
# REGISTER ROUTE
# -----------------------
@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        matric_no = request.form.get("matric_no")
        department = request.form.get("department")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")

        # ✅ Check duplicates
        existing_student = Student.query.filter(
            (Student.matric_no == matric_no) | (Student.email == email)
        ).first()
        if existing_student:
            flash("Matric No or Email already registered!", "danger")
            return redirect(url_for("auth.register"))

        # ✅ Create new student
        new_student = Student(
            full_name=full_name,
            matric_no=matric_no,
            department=department,
            email=email,
            phone=phone,
        )
        new_student.set_password(password)
        db.session.add(new_student)
        db.session.commit()

        flash("Registration successful! Please login.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


# -----------------------
# LOGIN ROUTE
# -----------------------
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        matric_no = request.form.get("matric_no")
        password = request.form.get("password")

        student = Student.query.filter_by(matric_no=matric_no).first()

        if student and student.check_password(password):
            login_user(student)  # ✅ Flask-Login logs in the user
            flash(f"Welcome back, {current_user.full_name}!", "success")
            return redirect(url_for("main.dashboard"))  # ✅ take to dashboard
            #return render_template("auth/login.html")  # ✅ reload same page, JS handles redirect

        else:
            flash("Invalid Matric No or Password", "danger")
            return redirect(url_for("auth.login"))  # ✅ reload login page
            

    return render_template("auth/login.html")


# -----------------------
# LOGOUT ROUTE
# -----------------------
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))
