# Documentation for Drug Classification Project

## Aim of the Project
The goal of this project is to predict the appropriate drug category for patients based on demographic and clinical features such as age, blood pressure, cholesterol levels, and sodium-to-potassium ratio. 

The data used for this project is sourced from [Kaggle](https://www.kaggle.com/datasets/prathamtripathi/drug-classification/data), which provides a labeled dataset containing 200 samples with detailed patient information.

This is a **multiclass classification task**, where the target variable represents different drug categories prescribed to patients.



---

## Steps to Find the Best Model
1. **Data Preparation**:
   - Cleaned and standardized the dataset for consistency.
   - Encoded categorical variables to ensure compatibility with machine learning models.

2. **Exploratory Data Analysis (EDA)**:
   - Investigated relationships between features and the target variable using statistical summaries and visualizations.

3. **Feature Engineering**:
   - Identified important features influencing the target variable using encoding methods and mutual information scores.

4. **Model Selection**:
   - Evaluated several models, including Logistic Regression, Decision Tree, Random Forest, and XGBoost.
   - Used SMOTE to handle class imbalances for underrepresented drug categories.
   - Selected the Decision Tree model for its simplicity and strong performance.

5. **Cross-Validation**:
   - Applied Stratified K-Fold to ensure the model performs consistently across the dataset.

---

## Encouragement to Explore the Notebook
This documentation provides a summary of the process. For detailed explanations of the methodologies, reasons behind decisions, and insights derived from the analysis, refer to the notebook file. It contains comprehensive breakdowns, visualizations, and parameter tuning steps.

---

## Finding, Context, and Takeaway Sections
In the notebook, you will find detailed explanations in the following sections:
- **Findings**: Specific observations about the data or model behavior, such as relationships between features and drug assignment.
- **Context**: Reasons behind decisions made during the project, such as why certain encoding methods or models were chosen.
- **Takeaways**: Summaries of key insights and learnings, like how SMOTE improved predictions for underrepresented drug categories.

These sections provide clarity on the thought process, justifications, and results behind the project, encouraging a deeper understanding of the work.
