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
