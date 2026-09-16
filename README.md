# 🌸 Iris Flower Detection & Classification

A Machine Learning based web application that predicts the species of an Iris flower from its sepal and petal measurements.

## 🚀 Project Overview

This project uses the **Iris Dataset** and a **Random Forest Classifier** to classify flowers into three species:

- Setosa
- Versicolor
- Virginica

The trained machine learning model is integrated with a **Flask web application** that provides predictions along with confidence probabilities.

## 🧠 Machine Learning

**Algorithm:** Random Forest Classifier

**Dataset:** Iris Dataset

**Features:**
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

**Classes:**
- Setosa
- Versicolor
- Virginica

## 📊 Model Performance

| Metric | Result |
|---|---:|
| Cross-Validation Accuracy | 96.19% |
| Final Test Accuracy | 95.65% |

The model was evaluated using accuracy, precision, recall, F1-score and confusion matrix.

## 🌐 Web Application

The Flask application allows users to enter the four flower measurements and get:

- Predicted flower species
- Prediction confidence
- Probability for each class

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML
- CSS

## 📁 Project Structure

```text
Iris-Flower-Detection-ML/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── README.md
