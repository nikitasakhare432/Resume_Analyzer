# Resume_Analyzer
# Live Demo: https://resume-analyzer-sckc.onrender.com/predict

# 🤖 AI Resume Analyzer + Job Role Predictor

An interactive Machine Learning web application that analyzes resume text and predicts the most suitable job role along with skill gap analysis and improvement suggestions.

---

## 🚀 Features

* 🔍 Predicts **job role** from resume text
* 📊 Shows **confidence score**
* 🧠 Calculates **resume strength score (out of 100)**
* ✅ Extracts **skills found** in resume
* ❌ Identifies **missing skills** for the predicted role
* 💡 Provides **suggestions to improve resume**
* 🎯 Interactive UI with progress bars and tags

---

## 🧠 Machine Learning Workflow

This project follows standard ML steps:

1. **Data Collection**

   * Resume dataset with labeled job categories

2. **Data Preprocessing**

   * Lowercasing
   * Removing special characters
   * Text cleaning

3. **Feature Engineering**

   * TF-IDF Vectorization

4. **Model Training**

   * Logistic Regression (Multiclass Classification)

5. **Model Evaluation**

   * Accuracy
   * Classification Report

6. **Model Deployment**

   * Flask Web App
   * Deployed on Render

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Flask
* **ML/NLP:** Scikit-learn (TF-IDF, Logistic Regression)
* **Deployment:** Render
* **Language:** Python

---

## 📂 Project Structure

```
resume-analyzer/
│
├── app.py
├── train_model.py
├── requirements.txt
├── model.pkl
├── vectorizer.pkl
├── label_encoder.pkl
├── resumes.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── .python-version
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd resume-analyzer
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🏋️‍♂️ Train the Model

```bash
python train_model.py
```

This will generate:

* `model.pkl`
* `vectorizer.pkl`
* `label_encoder.pkl`

---

## ▶️ Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🌐 Deployment (Render)

1. Push project to GitHub
2. Create new Web Service on Render
3. Use settings:

**Build Command**

```
pip install -r requirements.txt
```

**Start Command**

```
gunicorn app:app
```

4. Add `.python-version`

```
3.11.9
```

---

## 🧪 Sample Input

```
Python, SQL, Pandas, Machine Learning, Power BI, Excel
```

### Output:

* Predicted Role: Data Analyst
* Confidence: 82%
* Skills Found: Python, SQL, Excel
* Missing Skills: Tableau, Statistics

---

## 📈 Future Enhancements

* 📄 Resume PDF upload
* 📊 Resume vs Job Description matching
* 🧠 Top 3 role predictions
* 📚 Course recommendations
* 🌐 Better UI with Bootstrap
* 📊 Visualization dashboards

---

## 💡 Use Case

* Students improving resumes
* Freshers preparing for jobs
* Career guidance tools
* Resume screening systems

---

## 👩‍💻 Author

**Nikita Sakhare**

* 🎓 BE Computer Engineering (2022–2026)
* 📍 Pune, India
* 💻 Passionate about AI/ML & Full Stack Development

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share with others!
