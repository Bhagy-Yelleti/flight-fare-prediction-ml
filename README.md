# ✈️ Flight Fare Prediction – ML Web Application

🔗 **LinkedIn:** https://www.linkedin.com/in/bhagya-yelleti/  
🔗 **GitHub:** https://github.com/Bhagy-Yelleti  

---

## 📌 About the Project

**Flight Fare Prediction** is an end-to-end **Machine Learning web application** that predicts flight ticket prices based on user-provided travel details such as airline, source city, destination city, departure time, number of stops, duration, and days left for departure.

The project follows a **production-style ML pipeline**, integrating preprocessing, model inference using saved artifacts, and a Flask-based web interface for real-time predictions.

This repository represents a **significantly modified and extended version** of an open-source project, with major debugging, refactoring, dependency resolution, and deployment-readiness improvements implemented.

---

## 🚀 Features

- Web-based interface built using Flask  
- Modular ML pipeline (preprocessing → prediction)  
- Artifact-based model loading (`.pkl`)  
- Custom exception handling and logging  
- Clean `src/` project structure  
- Demo mode using dummy ML artifacts  
- MLOps tooling integration (DVC, MLflow)

---

## 🏗️ Project Structure

flight-fare-prediction-ml/
├── app.py # Flask application entry point
├── Artifacts/ # ML artifacts (ignored in git)
├── src/
│ └── FlightPricePrediction/
│ ├── components/ # Data ingestion & transformation
│ ├── pipeline/ # Training & prediction pipelines
│ ├── utils/ # Utility helpers
│ ├── exception.py # Custom exception handling
│ └── logger.py # Logging utilities
├── Notebook_Experiments/ # EDA & experimentation notebooks
├── static/ # Static assets
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

### Run Locally (Recommended)

#### 1. Clone the repository
```bash
git clone https://github.com/Bhagy-Yelleti/flight-fare-prediction-ml.git
cd flight-fare-prediction-ml
2. Create and activate a virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Generate dummy ML artifacts (demo mode)
bash
Copy code
python create_dummy_artifacts.py
5. Run the application
bash
Copy code
python app.py
Open in your browser:

arduino
Copy code
http://localhost:8080
🧠 How It Works
User submits flight details through the web UI

Input is transformed using a saved preprocessing pipeline

ML model predicts the flight fare

Result is rendered back on the frontend

The architecture cleanly separates training and inference, allowing models to be swapped without changing application logic.

📌 Notes
ML artifacts (.pkl) are intentionally excluded from version control

Dummy artifacts are used for UI and pipeline testing

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