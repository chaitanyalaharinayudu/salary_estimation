# salary_estimation
Project Description:

Title: **Salary Estimation Using Model Building Regression Techniques**

Problem Statement: Employees often lack adequate information to negotiate salaries during job interviews, especially when asked about salary expectations. This project aims to assist candidates by providing job role-specific salary predictions based on a dataset collected from approximately 1000 companies.

Proposed Solution: Develop an API that uses regression techniques to predict salaries. The solution will optimize multiple regression models, including linear, lasso, and random forest, to provide accurate salary estimations.

Modules:

Data Collection:
Description: Collect data from job postings, including job title, description, rating, company, location, salary range, etc., from websites like Glassdoor.

Data Cleaning:
Description: Clean the collected data to prepare it for analysis, creating new features and attributes as needed.

Data Analysis:
Description: Perform exploratory data analysis (EDA) to understand data distributions and value counts for categorical variables.

Model Building:
Description: Evaluate multiple regression models (multiple linear, lasso, random forest) using mean absolute error (MAE) as a performance metric.

API Building:

Description: Flask API endpoint that takes job listing data as input and returns estimated salaries.

Tools Used:
Python,
Anaconda, Spyder.
Packages:
selenium,
sklearn,
matplotlib,
seaborn,
pandas,
numpy,
flask,
json,
pickle.
