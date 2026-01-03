# ✈️ Flight Fare Prediction  
### End-to-End Machine Learning Web Application

🔗 **LinkedIn:** https://www.linkedin.com/in/bhagya-yelleti  
🔗 **GitHub:** https://github.com/Bhagy-Yelleti  

---

## 📌 Overview

**Flight Fare Prediction** is a production-style **Machine Learning web application** that predicts airline ticket prices based on real-world flight parameters such as airline, route, departure & arrival time, number of stops, travel duration, and days left before departure.

This project demonstrates how an ML model moves from experimentation to a usable web application using clean architecture, serialized pipelines, and a Flask-based interface.

This repository is a **significantly modified and extended version** of an open-source baseline, with major refactoring, debugging, dependency fixes, and deployment-readiness improvements.

---

## 🚀 Features

- Interactive Flask web interface  
- Modular ML pipeline (**training ≠ inference**)  
- Serialized preprocessing & model artifacts (`.pkl`)  
- Robust custom exception handling  
- Structured logging  
- Clean `src/`-based architecture  
- Demo mode using dummy artifacts  
- MLOps tooling with **DVC** & **MLflow**

---

## 🧠 How It Works

1. User enters flight details via the web UI  
2. Input is converted into a structured DataFrame  
3. Preprocessing pipeline transforms the data  
4. Trained ML model predicts the fare  
5. Result is rendered back to the UI  

The inference pipeline is fully decoupled from training, allowing models to be swapped without touching application code.

---

⚙️ TECH STACK
🧠 MACHINE LEARNING

scikit-learn — Model training & inference

Pandas, NumPy — Data processing & feature handling

🌐 BACKEND / WEB

Flask — Web application & API layer

📊 VISUALIZATION

Matplotlib

Seaborn

🔁 MLOPS & EXPERIMENT TRACKING

DVC — Data & pipeline versioning

MLflow — Experiment tracking & metrics

▶️ GETTING STARTED (RUN LOCALLY)
📥 1️⃣ CLONE THE REPOSITORY

git clone https://github.com/Bhagy-Yelleti/flight-fare-prediction-ml.git

cd flight-fare-prediction-ml

🧪 2️⃣ CREATE & ACTIVATE VIRTUAL ENVIRONMENT

python -m venv venv
venv\Scripts\activate

📦 3️⃣ INSTALL DEPENDENCIES

pip install -r requirements.txt

🧠 4️⃣ GENERATE DEMO ML ARTIFACTS

Required to run the app without retraining the model

python create_dummy_artifacts.py

🚀 5️⃣ RUN THE APPLICATION

python app.py

🌍 OPEN IN YOUR BROWSER

http://localhost:8080

🧠 HOW THE SYSTEM WORKS

📝 User enters flight details via the web UI
⬇️
🧮 Input is converted into a structured DataFrame
⬇️
⚙️ Preprocessing pipeline transforms the data
⬇️
📈 Trained ML model predicts the fare
⬇️
💰 Predicted price is displayed on the web interface

🔥 Training and inference are fully decoupled, meaning models can be swapped without touching application code.

📌 IMPORTANT NOTES

⚠️ ML artifacts (.pkl) are intentionally NOT committed to Git
🧪 Dummy artifacts enable UI & pipeline testing without retraining
🏋️ Full training can be enabled using real datasets
📂 Clean, production-style src/ architecture

📜 LICENSE & ATTRIBUTION

📄 Licensed under GNU General Public License v3.0 (GPL-3.0)

This project is a heavily modified and extended version of an open-source baseline originally authored by Kalyan M.

💥 MAJOR CONTRIBUTIONS BY BHAGYA YELLETI (2026)

Deep refactoring & critical bug fixes

Dependency & environment stabilization

Production-ready ML pipeline design

Deployment-friendly architecture

✔️ Original license terms are fully respected and preserved

👤 AUTHOR

👨‍💻 BHAGYA YELLETI
Machine Learning & Backend Developer

🔗 GitHub: https://github.com/Bhagy-Yelleti

🔗 LinkedIn: https://www.linkedin.com/in/bhagya-yelleti