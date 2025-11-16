# 🚢 Titanic Survival Prediction ML Project

[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/ASVATH2029/T-PROJ)](https://github.com/ASVATH2029/T-PROJ/commits/main)

---

## 📌 Overview
This is my **first Machine Learning project** using Python and scikit-learn.  
The project predicts whether a passenger survived the Titanic disaster based on features like age, sex, passenger class, and more.  

It demonstrates the **full ML pipeline**: data cleaning → feature engineering → model training → evaluation → saving the trained model.

---

## 📂 Project Structure

PROJECT 1/
│
├── data/
│ └── titanic.csv # Raw dataset
├── notebooks/
│ └── eda.ipynb # EDA & preprocessing
├── src/
│ ├── init.py
│ └── model.py # Save/load ML model
├── models/
│ └── titanic_model.pkl # Saved Logistic Regression model
└── requirements.txt # Python dependencies

---

## 📊 Dataset
- Source: [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic/data)  
- Features: `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`, `Embarked`  
- Target: `Survived` (0 = No, 1 = Yes)

---

## 🧹 Data Cleaning & Preprocessing
- Fill missing `Age` values with **median by passenger class**  
- Drop `Cabin` column (too many missing values)  
- Encode categorical features:
  - `Sex` → 0 (female), 1 (male)  
  - `Embarked` → 0 (S), 1 (C), 2 (Q)

---

## 🤖 Model
- **Logistic Regression**  
- Train-test split: 80% training / 20% testing  
- Achieved **accuracy: 82%** on the test set  

---

## 💾 Saving & Loading the Model
```python
from src.model import save_model, load_model

# Save trained model
save_model(model)

# Load model later
loaded_model = load_model()
🚀 Future Use Cases

Beginner ML portfolio project

Can extend to real-world binary classification problems:

Customer churn prediction

Loan default prediction

Disease survival prediction

Deployable as a web app or API for interactive predictions
🛠 How to Run

Clone the repo:

git clone https://github.com/ASVATH2029/T-PROJ.git


Install dependencies:

pip install -r requirements.txt


Open notebooks/eda.ipynb for EDA and model training

Use src/model.py to save/load the trained model
📋 Dependencies

Python 3.10+

pandas, numpy, scikit-learn, joblib

matplotlib / seaborn (for visualization)

✨ Author

Asvath (ajju)

3rd Year CSE Undergraduate

Passionate about Machine Learning and Python

GitHub Profile:https://github.com/ASVATH2029
