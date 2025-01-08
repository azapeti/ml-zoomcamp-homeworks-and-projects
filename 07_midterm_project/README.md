## Description of the Problem

This project is designed to predict employee attrition (i.e., whether an employee will leave the company) using various machine learning models. The data includes a variety of employee attributes, such as job role, work-life balance, age, education level, and many others. We will use this data to develop and evaluate different machine learning models, including decision trees, random forests, and XGBoost, to identify the factors contributing to employee attrition.

(The dataset used in this project is sourced from Kaggle. You can download it from the following link:
[Employee Attrition Dataset](https://www.kaggle.com/datasets/stealthtechnologies/employee-attrition-dataset))

### Key Goals:
- Perform exploratory data analysis (EDA) to understand the dataset and identify key features.
- Prepare the data for training by encoding categorical variables and splitting the data into training, validation, and test sets.
- Build and evaluate several machine learning models, comparing their performance using metrics like AUC, precision, recall, and F1 score.
- Tune the models to achieve the best performance using techniques like hyperparameter optimization.

## Instructions on How to Run the Project

### 1. **After downloading the repository**:
- Extract the contents of the repository.  
- Navigate to the folder in the terminal, e.g., `cd /path/to/where/you/downloaded/the-folder/folder`.


### 2. **Build the Docker Container**
   The model runs inside a Docker container. To build the Docker image, use the following command:

   ```bash
   docker build -t employee-attrition .
   ```

### 3. **Run the Docker Container**
   After building the Docker image, you can run the container with the following command:

   ```bash
   docker run -p 9696:9696 -it employee-attrition:latest
   ```

   This will start the container and expose the model on port 9696.

### 4. **Run the Prediction Script**
   Open a new terminal window and navigate to the project folder where the `predict_test.py` script is located. After the Docker container is running, you can use the `predict_test.py` script to test the model with a sample employee's data. This script contains test data for an employee, and running it will return the probability of attrition for that employee.

   ```bash
   python3 predict_test.py
   ```

   The script will output the probability of the employee leaving the company and whether the employee is predicted to attrite.
