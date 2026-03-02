from app import app
from db import db, Projects,Certificate

app.app_context().push()

p1 = Projects(
    title="Synapse Forge – Disease Prediction App",
    description="Synapse Forge demonstrates an end-to-end machine learning pipeline for predicting diseases based on user-provided symptoms. It showcases skills in data acquisition, text preprocessing, model training, evaluation, and interactive web application development using Streamlit.",
    image="project1.jpg",
    github="https://github.com/Kalpnaa/synapse-forge-project.git",
    demo=""
)

p2 = Projects(
    title="CreditClarity – Explainable AI Credit Risk Platform",
    description="Developed an Explainable AI-based credit risk prediction platform that analyzes financial data and provides transparent decision insights. Built as a full-stack Python application focusing on model interpretability and user-friendly visualization.",
    image="project2.jpg",
    github="https://github.com/Kalpnaa/credit_risk.git",
    demo=""
)

p3 = Projects(
    title="Zero-Shot Fake News Detector",
    description="Built a Zero-Shot Fake News Detection system using Large Language Models (LLMs) without requiring labeled training data. Implemented NLP and prompt engineering techniques to analyze news credibility and combat misinformation in real time.",
    image="project3.jpg",
    github="https://github.com/Kalpnaa/fake_news_llm.git",
    demo=""
)

db.session.add_all([p1, p2, p3])
db.session.commit()

print("Projects added successfully!")

c1 = Certificate(
    image="c1.jpg",
    title="AWS Academy Graduate - Machine Learning Foundations",
)


c2 = Certificate(
    image="c2.jpg",
    title="Oracle Cloud Infrastructure 2025 Certified AI Foundations Associate",
)


c3 = Certificate(
    image="c3.jpg",
    title="Hackerrank Skill Certificate for SQL(basic)",
)

c4= Certificate(
    image="c4.jpg",
    title="Hackerrank Skill Certificate for Python(basic)"
)

db.session.add_all([c1,c2,c3,c4])
db.session.commit()