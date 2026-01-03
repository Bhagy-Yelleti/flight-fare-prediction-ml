# ✈️ Flight Fare Prediction – ML Web Application

🔗 **LinkedIn:** https://www.linkedin.com/in/bhagya-yelleti/  
🔗 **GitHub:** https://github.com/Bhagy-Yelleti

---

## 📌 About The Project

**Flight Fare Prediction** is an end-to-end **Machine Learning web application** that predicts flight ticket prices based on user-provided travel details such as airline, source city, destination city, travel time, stops, duration, and days left for departure.

The project demonstrates a **production-style ML pipeline**, including preprocessing, model inference using saved artifacts, and a Flask-based web interface for real-time predictions.

This repository represents a **significantly modified and extended version** of an open-source project, with major debugging, refactoring, dependency resolution, and deployment-readiness improvements implemented.

---

## 🚀 Features

- Flask-based web application for flight fare prediction  
- Modular ML pipeline (data → preprocessing → prediction)  
- Artifact-based model loading (`.pkl`)  
- Custom exception handling and logging  
- Production-style `src/` project structure  
- Supports demo mode using dummy ML artifacts  
- MLOps tooling integration (DVC, MLflow)

---

## 🏗️ Project Structure

flight-fare-prediction-ml/
│
├── app.py # Flask application entry point
├── Artifacts/ # ML artifacts (ignored in git)
├── src/
│ └── FlightPricePrediction/
│ ├── components/ # Data ingestion & transformation
│ ├── pipeline/ # Training & prediction pipelines
│ ├── utils/ # Utility helpers
│ ├── exception.py # Custom exception handling
│ └── logger.py # Logging utilities
│
├── Notebook_Experiments/ # EDA & experimentation notebooks
├── static/ # Static assets
├── templates/ # HTML templates
├── requirements.txt
└── README.md

yaml
Copy code

---

## ⚙️ Tech Stack

- **Programming Language:** Python  
- **Web Framework:** Flask  
- **Machine Learning:** scikit-learn  
- **Data Handling:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn  
- **MLOps Tools:** DVC, MLflow  

---

## ▶️ Getting Started

### Option 1: Run Locally (Recommended)

#### 1️⃣ Clone the repository
```bash
git clone https://github.com/Bhagy-Yelleti/flight-fare-prediction-ml.git
cd flight-fare-prediction-ml
2️⃣ Create and activate virtual environment
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
Option 2: Docker (If Available)
bash
Copy code
docker pull kalyan45/flight-app
docker run -p 5000:5000 kalyan45/flight-app
🧠 How It Works
User submits flight details through the web UI

Input is transformed using a saved preprocessing pipeline

ML model predicts the flight fare

Result is rendered back on the frontend

The architecture cleanly separates training and inference, allowing models to be swapped without changing application logic.

📌 Notes
ML artifacts (.pkl) are intentionally excluded from version control

Dummy artifacts can be used for UI and pipeline testing

Real training can be enabled by providing a dataset and running the training pipeline

📜 License & Attribution
This project is released under the GNU General Public License v3.0 (GPL-3.0).

It is a modified and extended version of an open-source implementation originally authored by Kalyan M.

Significant modifications, debugging, refactoring, dependency resolution, and deployment-oriented improvements were implemented by Bhagya Yelleti (2026).

The project remains licensed under GPL-3.0 in full compliance with the original license.

👤 Author
Bhagya Yelleti
Machine Learning & Backend Developer

GitHub: https://github.com/Bhagy-Yelleti
LinkedIn: https://www.linkedin.com/in/bhagya-yelleti/

yaml
Copy code
