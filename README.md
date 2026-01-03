# Flight Fare Prediction

- LinkedIn [Bhagya Yelleti](https://www.linkedin.com/in/bhagya-yelleti/)

## About The Project

Welcome to the Flight Fare Prediction App! This project aims to provide users with a tool to predict flight fares based on various parameters, allowing them to make informed decisions when booking air travel. The app utilizes machine learning algorithms trained on historical flight data to estimate future fares. Users can input details such as departure and arrival locations, date, and airline preferences to receive an estimated fare for their desired flight. Whether you're a frequent traveller or planning your next vacation, this app is designed to make the flight booking process more transparent and efficient. Feel free to explore, contribute, and enhance the functionality of this Flight Fare Prediction App!

## Built With

 - Pandas
 - Numpy
 - Scikit-learn
 - Seaborn
 - Matplotlib
 - Flask
 - DVC
 - MLFlow

## Getting Started

This will help you understand how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Installation Steps

### Option 1: Installation from GitHub

Follow these steps to install and set up the project directly from the GitHub repository:

1. **Clone the Repository**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to install the project.
   - Run the following command to clone the GitHub repository:
     ```
     git clone https://github.com/KalyanMurapaka45/Flight-Fare-Prediction.git
     ```

2. **Create a Virtual Environment** (Optional but recommended)
   - It's a good practice to create a virtual environment to manage project dependencies. Run the following command:
     ```
     conda create -p <Environment_Name> python==<python version> -y
     ```

3. **Activate the Virtual Environment** (Optional)
   - Activate the virtual environment based on your operating system:
       ```
       conda activate <Environment_Name>/
       ```

4. **Install Dependencies**
   - Navigate to the project directory:
     ```
     cd [project_directory]
     ```
   - Run the following command to install project dependencies:
     ```
     pip install -r requirements.txt
     ```

5. **Run the Project**
   - Start the project by running the appropriate command.
     ```
     python app.py
     ```

6. **Access the Project**
   - Open a web browser or the appropriate client to access the project.
  
<br><br>
### Option 2: Installation from DockerHub

If you prefer to use Docker, you can install and run the project using a Docker container from DockerHub:

1. **Pull the Docker Image**
   - Open your terminal or command prompt.
   - Run the following command to pull the Docker image from DockerHub:
     ```
     docker pull kalyan45/flight-app
     ```

2. **Run the Docker Container**
   - Start the Docker container by running the following command, and mapping any necessary ports:
     ```
     docker run -p 5000:5000 kalyan45/flight-app
     ```

3. **Access the Project**
   - Open a web browser or the appropriate client to access the project.






