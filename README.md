# PCOS Self-Assessment Web App

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Flask-black.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

A user-friendly, multi-step web application built with Flask that allows users to perform a self-assessment for Polycystic Ovary Syndrome (PCOS). The application uses a pre-trained machine learning model to predict the risk of PCOS based on user-inputted health data, providing an instant and intuitive result.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## ✨ Features

* **Interactive Multi-Step Form**: A guided, multi-step questionnaire that collects user health data in a structured and user-friendly manner.
* **Machine Learning Integration**: Utilizes a `scikit-learn` model (`.pkl`) to provide real-time predictions based on user inputs.
* **Dynamic BMI Calculation**: Automatically calculates and displays the Body Mass Index (BMI) and its category (e.g., Normal, Overweight) as the user enters their weight and height.
* **Instant Results**: Displays the assessment result immediately upon form submission, indicating either "Risk of PCOS" or "No Risk of PCOS".
* **Confidence Score**: Presents a probability score to show the model's confidence in its prediction.
* **Data Summary**: Provides a clear summary of the user's submitted health profile on the results page.
* **Responsive Design**: A clean, modern, and responsive user interface styled with CSS, ensuring usability across different devices.
* **Printable Results**: Allows users to save or print their assessment results directly from the browser.

---

## 📚 Table of Contents

* [How It Works](#-how-it-works)
* [Technical Stack](#-technical-stack)
* [Project Structure](#-project-structure)
* [Installation](#-installation)
* [Usage](#-usage)
* [Model & Features](#-model--features)
* [Contributing](#-contributing)
* [License](#-license)

---

## ⚙️ How It Works

The application guides the user through a three-step form:
1.  **Basic Information**: Collects age, weight, and height, and auto-calculates BMI.
2.  **Cycle Information**: Gathers details about menstrual cycle length and regularity.
3.  **Symptoms**: Asks about common PCOS symptoms like weight gain, hair growth, skin darkening, and pimples.

Once the form is submitted, the data is preprocessed and fed into a loaded `pcos_self_assess_model.pkl` model. The model predicts the outcome and the probability, which are then displayed on a dedicated results page.

---

## 💻 Technical Stack

* **Backend**: Flask
* **Machine Learning**: Scikit-learn, Pandas, NumPy
* **Frontend**: HTML, CSS, JavaScript (for form logic)
* **Deployment**: Can be deployed using any WSGI server like Gunicorn.

---

## 🏛️ Project Structure

The project follows a standard Flask application structure.

## 🚀 Installation

Follow these steps to set up and run the project locally.

### Prerequisites

* Python 3.x
* A pre-trained model file named `pcos_self_assess_model.pkl` in the root directory.

### Step-by-Step Guide

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Unix/macOS
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ensure the model is in place:**
    Make sure you have the `pcos_self_assess_model.pkl` file in the root directory of the project. The application will fail to start without it.

---

## 🛠️ Usage

Once the installation is complete, you can run the Flask development server.

```bash
flask run


