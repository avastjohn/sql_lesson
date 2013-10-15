from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

@app.route("/")
def get_github():
    return render_template("get_github.html",)

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("student")
    row = hackbright_app.get_student_by_github(student_github)
    rows = hackbright_app.get_student_report(student_github)
    html = render_template("student_info.html", first_name = row[0],
                                                last_name = row [1],
                                                github = row[2],
                                                projects = rows
                                                )
    return html

@app.route("/projects")
def get_projects():
    hackbright_app.connect_to_db()
    project = request.args.get("project")
    rows = hackbright_app.get_project_grades(project)
    html = render_template("project_info.html", project_title = project,
        project_grades = rows
        )
    return html

@app.route("/newstudent")
def create_student_record():
    hackbright_app.connect_to_db()
    new_first_name = request.args.get("first_name")
    new_last_name = request.args.get("last_name")
    new_github = request.args.get("github")
    hackbright_app.make_new_student(new_first_name, new_last_name, new_github)
    html = render_template("student_info.html", first_name = new_first_name, last_name = new_last_name, github = new_github)
    return html

@app.route("/newproject")
def create_project_record():
    hackbright_app.connect_to_db()
    new_title = request.args.get("title")
    new_description = request.args.get("description")
    new_max_grade = request.args.get("max_grade")
    hackbright_app.make_new_project(new_title, new_description, new_max_grade)
    html = render_template("project_info.html", project_title = new_title)
    return html

@app.route("/assigngrade")
def create_grade_record():
    hackbright_app.connect_to_db()
    new_github = request.args.get("student_github")
    new_title = request.args.get("project_title")
    new_grade = request.args.get("grade")
    hackbright_app.assign_grade(new_github, new_title, new_grade)
    html = render_template("project_info.html", project_title = new_title)
    return html




if __name__ == "__main__":
    app.run(debug=True)