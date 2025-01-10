## Table of Contents

- [Aim of the project](#aim-of-the-project)
- [Steps to find the best model](#steps-to-find-the-best-model)
  - Data preparation
  - Exploratory data analysis (EDA)
  - Feature engineering
  - Model selection
  - Cross-validation

- [Encouragement to explore the notebook](#encouragement-to-explore-the-notebook)
- [Finding, Context, and Takeaway sections](#finding-context-and-takeaway-sections)
- [Running the project in a Docker container](#running-the-project-in-a-docker-container)
  - [Steps to run the project](#steps-to-run-the-project)
  - [Benefits of using Docker](#benefits-of-using-docker)


# Documentation for Drug Classification Project

## Aim of the project
The goal of this project is to predict the appropriate drug category for patients based on demographic and clinical features such as age, blood pressure, cholesterol levels, and sodium-to-potassium ratio. 

The data used for this project is sourced from [Kaggle](https://www.kaggle.com/datasets/prathamtripathi/drug-classification/data), which provides a labeled dataset containing 200 samples with detailed patient information.

This is a **multiclass classification task**, where the target variable represents different drug categories prescribed to patients.

---

## Steps to find the best model
1. **Data preparation**:
   - Cleaned and standardized the dataset for consistency.
   - Encoded categorical variables to ensure compatibility with machine learning models.

2. **Exploratory Data Analysis (EDA)**:
   - Investigated relationships between features and the target variable using statistical summaries and visualizations.

3. **Feature engineering**:
   - Identified important features influencing the target variable using encoding methods and mutual information scores.

4. **Model selection**:
   - Evaluated several models, including Logistic Regression, Decision Tree, Random Forest, and XGBoost.
   - Used SMOTE to handle class imbalances for underrepresented drug categories.
   - Selected the Decision Tree model for its simplicity and strong performance.

5. **Cross-Validation**:
   - Applied Stratified K-Fold to ensure the model performs consistently across the dataset.

---

## Encouragement to explore the notebook
This documentation provides a summary of the process. For detailed explanations of the methodologies, reasons behind decisions, and insights derived from the analysis, refer to the notebook file. It contains comprehensive breakdowns, visualizations, and parameter tuning steps.

---

## Finding, Context, and Takeaway sections
In the notebook, you will find detailed explanations in the following sections:
- **Findings**: Specific observations about the data or model behavior, such as relationships between features and drug assignment.
- **Context**: Reasons behind decisions made during the project, such as why certain encoding methods or models were chosen.
- **Takeaways**: Summaries of key insights and learnings, like how SMOTE improved predictions for underrepresented drug categories.

These sections provide clarity on the thought process, justifications, and results behind the project, encouraging a deeper understanding of the work.

---

## Running the project in a Docker container

The project is designed to run in a **Docker container** for ease of setup and consistency. Ensure that Docker is installed and running on your machine before proceeding.

### Steps to run the project
1. **Pull the base Docker image**:
   ```bash
   docker run -it --rm python:3.12.8-slim
   
2. **Build the Docker container**:
   ```bash
   docker build -t drug-classification .

3. **Run the Docker container**:
   ```bash
   docker run -it --rm -p 9696:9696 drug-classification

4. **Run the Prediction Script**:

   Open a new terminal window and navigate to the project folder where the `predict_test.py` script is located. After the Docker container   is running, you can use the `predict_test.py` script to test the model with a sample data of patients. This script contains test data for three patients, and running it will return the proposed drug.

   ```bash
   python3 predict_test.py
   ```

### Benefits of using Docker
- **Consistency**: Ensures the same environment across all machines.
- **Dependency Management**: No need to manually install or configure dependencies.
- **Portability**: Easily share and replicate the setup.


