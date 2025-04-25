# 🏠 Price Predictor System

A machine learning project for predicting house prices using the Ames Housing dataset. This end-to-end system includes data preprocessing, model training, and price prediction, built with Python and scikit-learn. Designed as a portfolio project for data science learners and resume showcases.

---

## 📊 Project Highlights

- 📦 End-to-end pipeline from training to prediction  
- 🧠 ML model built using scikit-learn  
- 📁 Uses AmesHousing dataset (CSV extracted from a ZIP)  
- 📈 MLflow integration for experiment tracking  
- 📊 In-depth exploratory data analysis  
- 🧪 Unit testing and modular code structure  

---

## 🔧 Tech Stack

- **Language & Libraries:** Python, scikit-learn, Pandas, NumPy, Matplotlib, Seaborn  
- **Experiment Tracking:** MLflow  
- **Configuration:** YAML (`config.yaml`)  
- **Project Structure:** Modular ML pipelines  

---

## 🗂 Project Structure

```text
.
├── data/                  # Contains archive.zip (original dataset)
├── extracted_data/        # Contains AmesHousing.csv (extracted)
├── analysis/              # Jupyter notebooks and EDA
├── pipelines/             # Data processing and model pipelines
├── src/                   # Core source code
├── steps/                 # ML pipeline steps
├── run_pipeline.py        # Training pipeline script
├── sample_predict.py      # Prediction script
├── requirements.txt       # Project dependencies
├── config.yaml            # Configuration file
├── mlruns/                # MLflow experiment logs
├── tests/                 # Unit tests
└── README.md              # This file
```

## 🚀 Getting Started

1. Clone the repository

    ```bash
    git clone <(https://github.com/TechFox6905/prices-predictor-system.git)>
    cd prices-predictor-system
    ```

2. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Training Pipeline

    This will load the data, preprocess it, train the model, and log to MLflow.

    ```bash
    python run_pipeline.py
    ```

4. Make Predictions

    Use the trained model to predict house prices:

    ```bash
    python sample_predict.py
    ```

---

## 📈 MLflow Tracking

The project logs training runs to MLflow. While MLflow is set up for local tracking, deployment to a remote server is currently not enabled due to deployment errors.

---

## 📊 Exploratory Data Analysis

Explore the `analysis/` folder for insightful visualizations and feature exploration using the AmesHousing dataset.

---

## 📌 Purpose

This project was built as a **portfolio piece** to demonstrate skills in:

- End-to-end machine learning workflows  
- Data analysis and visualization  
- Model deployment (WIP)  
- Best practices in structuring ML projects  

---

## 🧠 Future Improvements

- 🛰️ Fix deployment issues and deploy MLflow tracking server  
- 🌐 Build a web UI using Streamlit or Flask  
- 🏗️ Add more model options and hyperparameter tuning 
