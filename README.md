#  Cognitive Wellness AI Companion

##  Overview
The **Cognitive Wellness AI Companion** is a machine learning–powered web application that promotes mental clarity and productivity.  
It analyzes user inputs — **mood/thoughts, step count, and heart rate** — to classify cognitive states (e.g., *Stressed, Fatigued, Creative, Focused*) and delivers personalized micro‑activity recommendations.

This project demonstrates **end‑to‑end ML engineering, feature extraction, recommendation systems, and deployment with Flask + Docker**, making it a strong portfolio piece.

---

##  Features
- **Signals:** Text input, step count, heart rate  
- **State Classification:** Rule‑based + ML classifier for 50+ states  
- **Recommendation Engine:** JSON‑based micro‑activity database  
- **Frontend:** Flask + HTML/CSS with modern UI styling  
- **EDA Notebook:** Exploratory data analysis with pandas, seaborn, matplotlib  
- **Deployment:** Dockerized for portability  



---

##  Project Structure

```text
COGNITIVE WELLNESS/
├── backend/
│   ├── recommender/
│   │   ├── activity_db.json    # Database of wellness activities & metadata
│   │   └── rl_engine.py         # Reinforcement Learning logic for personalized recs
│   ├── utils/
│   │   └── state_classifier.py  # ML model to classify cognitive/emotional states
│   └── app.py                  # Flask/FastAPI server connecting backend to UI
├── notebooks/
│   └── eda.py                  # Exploratory Data Analysis & prototyping (converted script)
├── static/
│   └── style.css               # Frontend styling
├── templates/
│   └── index.html              # Main dashboard user interface
└── requirements.txt            # Project dependencies (NumPy, Scikit-learn, Flask, etc.)
