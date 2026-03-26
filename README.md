#  Cognitive Wellness AI Companion

A machine learning-powered web application designed to enhance mental clarity and productivity. By analyzing physiological signals and user sentiment, the system classifies cognitive states (e.g., *Stressed, Fatigued, Focused*) and provides personalized micro-activity recommendations.

---

##  Key Features

* **Multimodal Analysis:** Integrates text-based mood/thoughts with physical data (Step Count & Heart Rate).
* **State Classification:** Uses a hybrid Rule-based + ML classifier to identify 50+ unique cognitive/emotional states.
* **Intelligent Recommendations:** Powered by a Reinforcement Learning (RL) engine that adapts to user feedback over time.
* **Data-Driven Insights:** Includes an Exploratory Data Analysis (EDA) suite for visualizing wellness trends.
* **Modern UI:** Responsive dashboard built with Flask, HTML5, and CSS3.

---

##  Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn, NumPy, Pandas
* **Personalization:** Reinforcement Learning (Custom RL Engine)
* **Data Visualization:** Matplotlib, Seaborn
* **DevOps:** Docker (Optional), Requirements-based Environment

---
## Install dependencies
* pip install -r requirements.txt
* python backend/app.py
* python notebooks/eda.py

##  Project Structure

```text
COGNITIVE WELLNESS/
├── backend/
│   ├── recommender/
│   │   ├── activity_db.json     # JSON database of wellness activities
│   │   └── rl_engine.py         # Reinforcement Learning logic for recs
│   ├── utils/
│   │   └── state_classifier.py  # ML model for cognitive state classification
│   └── app.py                   # Main Flask server (Entry Point)
├── notebooks/
│   └── eda.py                   # EDA & Prototyping script
├── static/
│   └── style.css                # Dashboard styling
├── templates/
│   └── index.html               # Frontend User Interface
└── requirements.txt             # Project dependencies
