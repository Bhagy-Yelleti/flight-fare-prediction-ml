# ✈️ Flight Fare Prediction  
### End-to-End Machine Learning Web Application

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Flask-Web_App-black?logo=flask" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange" />
  <img src="https://img.shields.io/badge/MLOps-DVC%20%7C%20MLflow-purple" />
  <img src="https://img.shields.io/badge/License-GPL--3.0-green" />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/bhagya-yelleti/">LinkedIn</a> ·
  <a href="https://github.com/Bhagy-Yelleti">GitHub</a>
</p>

---

## 📌 Overview

**Flight Fare Prediction** is a production-style **Machine Learning web application** that predicts airline ticket prices based on real-world flight parameters such as airline, route, departure/arrival time, number of stops, travel duration, and days left before departure.

The project demonstrates how an ML model is taken **from experimentation to a usable web application**, with proper preprocessing pipelines, serialized artifacts, modular code structure, and a clean Flask interface.

This repository represents a **significantly modified and extended version** of an open-source baseline. Major refactoring, debugging, dependency fixes, and deployment-readiness improvements have been implemented.

---

## 🚀 Features

- Interactive Flask web interface  
- Modular ML pipeline (training ≠ inference)  
- Serialized preprocessing & model artifacts (`.pkl`)  
- Robust custom exception handling  
- Structured logging  
- Clean `src/`-based architecture  
- Demo mode support using dummy artifacts  
- MLOps tooling with DVC & MLflow  

---

## 🧠 How It Works

1. User enters flight details via the web form  
2. Input is converted into a structured DataFrame  
3. Preprocessing pipeline transforms the data  
4. Trained ML model predicts the fare  
5. Result is rendered back to the UI  

The inference pipeline is **fully decoupled** from training, allowing models to be swapped without touching application code.

---

## 🧱 Project Structure

flight-fare-prediction-ml/
├── app.py # Flask app entry point
├── Artifacts/ # ML artifacts (ignored in git)
├── src/
│ └── FlightPricePrediction/
│ ├── components/ # Data ingestion & transformation
│ ├── pipeline/ # Training & prediction pipelines
│ ├── utils/ # Utility functions
│ ├── exception.py # Custom exception handling
│ └── logger.py # Logging setup
├── Notebook_Experiments/ # EDA & model experiments
├── static/ # Static files (CSS, assets)
├── templates/ # HTML templates
├── requirements.txt
└── README.md

yaml
Copy code

---

## ⚙️ Tech Stack

- **Language:** Python  
- **Web Framework:** Flask  
- **Machine Learning:** scikit-learn  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn  
- **MLOps:** DVC, MLflow  

---

## ▶️ Getting Started

### Run Locally

#### 1️⃣ Clone the repository
```bash
git clone https://github.com/Bhagy-Yelleti/flight-fare-prediction-ml.git
cd flight-fare-prediction-ml
2️⃣ Create & activate virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ (Demo Mode) Generate dummy ML artifacts
bash
Copy code
python create_dummy_artifacts.py
5️⃣ Run the application
bash
Copy code
python app.py
Open in browser:

arduino
Copy code
http://localhost:8080


📌 Notes
ML artifacts are intentionally excluded from version control

Dummy artifacts allow UI & pipeline testing without retraining

Full training can be enabled by providing the dataset and running the training pipeline

📜 License & Attribution
This project is licensed under the GNU General Public License v3.0 (GPL-3.0).

It is a modified and extended version of an open-source project originally authored by Kalyan M.

Significant refactoring, debugging, dependency resolution, and deployment-oriented improvements were implemented by Bhagya Yelleti (2026).

License terms are fully respected and preserved.

👤 Author
Bhagya Yelleti
Machine Learning & Backend Developer

GitHub: https://github.com/Bhagy-Yelleti

LinkedIn: https://www.linkedin.com/in/bhagya-yelleti/

yaml
Copy code
