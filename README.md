🐞 Insect Classification 🗃️

🚀 Welcome to my Insect Classification project! This challenge was part of a #CodingChallenge on NUWE, where I had to develop a machine learning model to classify different species of insects based on sensor data. 🌱🐜

🏆 Challenge Overview

Category: Data Science
Subcategory: Machine Learning Engineer
Difficulty: Easy
Expected Solution Time: ⏳ 3 hours

In this project, I built a classification model to predict insect species using environmental sensor readings. The goal? To contribute to biodiversity conservation by automating insect identification in different habitats! 🦋🌿

🌐 Background

Biodiversity conservation is crucial, and insects play a vital role in maintaining ecological balance. This challenge aimed to classify insects based on environmental sensor data, helping scientists monitor populations and protect species more effectively.

🗂️ Dataset

The dataset consists of two files:

📌 train.csv – Contains sensor readings and corresponding insect categories.
📌 test.csv – Includes sensor data without labels (for model predictions).

Features:
Sensor_alpha, Sensor_beta, Sensor_gamma: Continuous environmental sensor readings.
Hour, Minutes: Time variables for when the measurements were taken.
Insect: Categorical label (only present in the training set).
⚠️ Important: Time is a cyclic feature! Since machine learning models don’t naturally understand cyclical patterns, I transformed time features using sine and cosine functions in #NumPy to improve generalization. 🔄

📊 Data Processing

To ensure optimal model performance, I applied:
✅ Feature scaling for continuous sensor values.
✅ Time encoding using sine and cosine transformations.
✅ Data cleaning and preprocessing.

🤖 Model

The challenge allowed for flexibility in model selection. I experimented with different classifiers and optimized performance using:

Random Forest 🌲
Decision Trees 🌳
Ensemble Learning 🤖
Final model selection was based on F1 Score, ensuring a balance between precision and recall.

📂 Repository Structure

|__ README.md
|__ requirements.txt
|
|__ data
|  |__ train.csv
|  |__ test.csv
|
|__ src
|  |__ data_processing.py
|  |__ model_training.py
|  |__ model_prediction.py
|  |__ utils.py
|
|__ models
|  |__ model.pkl
|
|__ scripts
|  |__ run_pipeline.sh
|
|__ predictions
   |__ example_predictions.json
   |__ predictions.json

🔹 Key Components:
📌 src/ – Contains scripts for data preprocessing, model training, and predictions.
📌 models/ – Stores the trained classification model.
📌 scripts/ – Includes run_pipeline.sh, an automation script for workflow execution.
📌 predictions/ – Stores output predictions in JSON format.

💡 Automation Tip: I used .sh scripts to streamline the workflow! This was a great learning experience in modularizing ML pipelines. 🛠️

🎯 Tasks

✔️ Task 1: Develop a model that classifies insects into categories (0, 1, or 2) using sensor data.
✔️ Task 2: Format predictions correctly in predictions.json:

{
    "target": {
        "1": 0,
        "2": 3,
        "3": 8,
        "4": 5,
        "5": 2
    }
}

📊 Evaluation

📌 Metric: F1 Score – A balanced measure of precision and recall.
📌 Goal: Achieve the highest F1 Score for accurate insect classification.

✅ Best practices:

Feature engineering for better generalization.
Experimenting with different ML models.
Fine-tuning hyperparameters for optimal performance.
📤 Submission

The final submission consists of:
📌 Trained model: model.pkl
📌 Predictions: predictions.json

❓ FAQs

Q: What is the goal of this challenge?
A: To develop a model that classifies insects based on sensor data, helping in conservation efforts.

Q: What ML algorithms are recommended?
A: You can use decision trees, random forests, or even deep learning. Choose the best fit for the problem!

Q: How are predictions evaluated?
A: Using the F1 Score, which balances precision and recall for classification performance.

🌟 Final Thoughts

This challenge was an exciting opportunity to apply machine learning in ecology, improve my workflow automation skills, and explore feature engineering for time-based data.

If you're interested in this project, feel free to explore my GitHub repo or connect with me on LinkedIn! 🚀🔗 www.linkedin.com/in/nathan-jo 