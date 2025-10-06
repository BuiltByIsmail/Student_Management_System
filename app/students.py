from flask import Blueprint, render_template, request, redirect, url_for, flash
from .extensions import db
from .models import Student
from flask_login import login_required

students_bp = Blueprint("students", __name__, template_folder="../templates/students")

@students_bp.route("/")
@login_required
def list_students():
    q = request.args.get("q", "")
    if q:
        students = Student.query.filter(
            (Student.name.ilike(f"%{q}%")) |
            (Student.student_id.ilike(f"%{q}%")) |
            (Student.department.ilike(f"%{q}%"))
        ).all()
    else:
        students = Student.query.all()
    return render_template("students/list.html", students=students, q=q)

@students_bp.route("/add", methods=["GET","POST"])
@login_required
def add_student():
    if request.method == "POST":
        student_id = request.form.get("student_id")
        name = request.form.get("name")
        department = request.form.get("department")
        email = request.form.get("email")
        phone = request.form.get("phone")

        # basic server-side validation
        if not (student_id and name and department and email):
            flash("Student ID, name, department and email are required.", "danger")
            return redirect(url_for("students.add_student"))

        if Student.query.filter_by(student_id=student_id).first():
            flash("Student ID already exists.", "warning")
            return redirect(url_for("students.add_student"))

        if Student.query.filter_by(email=email).first():
            flash("Email already used.", "warning")
            return redirect(url_for("students.add_student"))

        s = Student(student_id=student_id, name=name, department=department, email=email, phone=phone)
        db.session.add(s)
        db.session.commit()
        flash("Student added.", "success")
        return redirect(url_for("students.list_students"))
    return render_template("students/add.html")

@students_bp.route("/update/<int:id>", methods=["GET","POST"])
@login_required
def update_student(id):
    s = Student.query.get_or_404(id)
    if request.method == "POST":
        s.student_id = request.form.get("student_id")
        s.name = request.form.get("name")
        s.department = request.form.get("department")
        s.email = request.form.get("email")
        s.phone = request.form.get("phone")
        db.session.commit()
        flash("Student updated.", "success")
        return redirect(url_for("students.list_students"))
    return render_template("students/update.html", student=s)

@students_bp.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete_student(id):
    s = Student.query.get_or_404(id)
    db.session.delete(s)
    db.session.commit()
    flash("Student deleted.", "info")
    return redirect(url_for("students.list_students"))
