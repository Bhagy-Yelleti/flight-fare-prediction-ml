✈️ Flight Fare Prediction
End-to-End Machine Learning Web Application

🔗 LinkedIn: https://www.linkedin.com/in/bhagya-yelleti

🔗 GitHub: https://github.com/Bhagy-Yelleti

📌 Overview

Flight Fare Prediction is a production-style Machine Learning web application that predicts airline ticket prices based on real-world flight parameters such as airline, route, departure & arrival time, number of stops, travel duration, and days left before departure.

This project demonstrates how an ML model moves from experimentation to a usable web application using clean architecture, serialized pipelines, and a Flask-based interface.

This repository is a significantly modified and extended version of an open-source baseline, with major refactoring, debugging, dependency fixes, and deployment-readiness improvements.

🚀 Features

Interactive Flask web interface

Modular ML pipeline (training ≠ inference)

Serialized preprocessing & model artifacts (.pkl)

Robust custom exception handling

Structured logging

Clean src/-based architecture

Demo mode using dummy artifacts

MLOps tooling with DVC & MLflow

🧠 How It Works

User enters flight details via the web UI

Input is converted into a structured DataFrame

Preprocessing pipeline transforms the data

Trained ML model predicts the fare

Result is rendered back to the UI

The inference pipeline is fully decoupled from training, allowing models to be swapped without touching application code.

🧱 Project Structure
flight-fare-prediction-ml/
├── app.py                     # Flask app entry point
├── Artifacts/                 # ML artifacts (git-ignored)
├── src/
│   └── FlightPricePrediction/
│       ├── components/        # Data ingestion & transformation
│       ├── pipeline/          # Training & prediction pipelines
│       ├── utils/             # Utility helpers
│       ├── exception.py       # Custom exceptions
│       └── logger.py          # Logging setup
├── Notebook_Experiments/      # EDA & experimentation
├── static/                    # Static assets
├── templates/                 # HTML templates
├── requirements.txt
└── README.md

⚙️ Tech Stack

Language: Python

Web Framework: Flask

Machine Learning: scikit-learn

Data Processing: Pandas, NumPy

Visualization: Matplotlib, Seaborn

MLOps: DVC, MLflow

▶️ Getting Started
Run Locally
1️⃣ Clone the repository
git clone https://github.com/Bhagy-Yelleti/flight-fare-prediction-ml.git
cd flight-fare-prediction-ml

2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Generate demo ML artifacts
python create_dummy_artifacts.py

5️⃣ Run the application
python app.py


Open in browser:

http://localhost:8080

📌 Notes

ML artifacts are intentionally excluded from version control

Dummy artifacts allow UI & pipeline testing without retraining

Full training can be enabled by providing a dataset and running the training pipeline

📜 License & Attribution

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).

It is a modified and extended version of an open-source project originally authored by Kalyan M.

Significant refactoring, debugging, dependency resolution, and deployment-oriented improvements were implemented by Bhagya Yelleti (2026).

License terms are fully respected and preserved.

👤 Author

Bhagya Yelleti
Machine Learning & Backend Developer

🔗 GitHub: https://github.com/Bhagy-Yelleti

🔗 LinkedIn: https://www.linkedin.com/in/bhagya-yelleti