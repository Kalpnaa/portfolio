from flask import Flask, render_template
from db import db, Projects, Certificate, Experience


app = Flask(__name__)

# DATABASE CONFIG (missing in your code)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connect db with app
db.init_app(app)
@app.route('/')
def main():
    projects = Projects.query.all()
    certificates = Certificate.query.all()
    experiences = Experience.query.all()

    return render_template(
        "index.html",
        projects=projects,
        certificates=certificates,
        experiences=experiences
    )

if __name__ == "__main__":
    with app.app_context():
        db.create_all()   # THIS creates table
    app.run(debug=True)