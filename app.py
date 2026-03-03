from flask import Flask, render_template
from db import db, Projects, Certificate, Experience
import os

app = Flask(__name__)

# Use old DB locally, Render path on server
if os.environ.get("RENDER"):
    db_path = "/opt/render/project/src/site.db"
else:
    db_path = "site.db"   # your old DB with data

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
    app.run()