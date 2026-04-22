from flask import Flask, render_template, request
import pickle
import re
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

app = Flask(__name__)

# Load model files
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Skill database
role_skills = {
    "Data Analyst": ["python", "sql", "excel", "power bi", "tableau", "statistics", "pandas"],
    "Data Scientist": ["python", "machine learning", "deep learning", "nlp", "tensorflow", "pandas"],
    "Web Developer": ["html", "css", "javascript", "react", "bootstrap", "frontend"],
    "Java Developer": ["java", "spring boot", "hibernate", "mysql", "rest api", "jdbc"],
    "Python Developer": ["python", "django", "flask", "api", "backend", "postgresql"],
    "ML Engineer": ["python", "scikit", "machine learning", "tensorflow", "deep learning", "deployment"],
    "Full Stack Developer": ["html", "css", "javascript", "react", "node", "express", "mongodb"]
}

def extract_skills(resume_text):
    resume_lower = resume_text.lower()
    found_skills = []

    all_skills = set()
    for skills in role_skills.values():
        for skill in skills:
            all_skills.add(skill)

    for skill in all_skills:
        if skill in resume_lower:
            found_skills.append(skill)

    return found_skills

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    resume_text = request.form["resume"]

    cleaned = clean_text(resume_text)
    vectorized = vectorizer.transform([cleaned])

    prediction = model.predict(vectorized)[0]
    predicted_role = label_encoder.inverse_transform([prediction])[0]

    if hasattr(model, "predict_proba"):
        confidence = max(model.predict_proba(vectorized)[0]) * 100
    else:
        confidence = 0

    found_skills = extract_skills(resume_text)

    expected_skills = role_skills.get(predicted_role, [])
    missing_skills = [skill for skill in expected_skills if skill not in [s.lower() for s in found_skills]]

    score = min(len(found_skills) * 10, 100)

    return render_template(
        "index.html",
        prediction=predicted_role,
        confidence=round(confidence, 2),
        found_skills=found_skills,
        missing_skills=missing_skills,
        score=score,
        resume_text=resume_text
    )

if __name__ == "__main__":
    app.run(debug=True)