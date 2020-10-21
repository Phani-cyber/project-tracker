"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    github = request.form.get('github')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    
    return render_template("student_add.html")

@app.route("/stu")
def adding_title_and_grade():
    title = request.args.get('title')

    title = hackbright.get_project_by_title(title)

    github = request.args.get('github')

    grades = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           title=title,
                           grades=grades)
    return html



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
