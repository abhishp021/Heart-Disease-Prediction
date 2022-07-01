# Heart-Disease-Prediction

## [App Link](https://heart--disease--predictions.herokuapp.com/)

## Table of Contents
### [1. Dataset](#dataset)
### [2. Data Exploration](#data-exploration)
### [3. Data Preprocessing](#data-preprocessing)
### [4. Train-Test Splitting](#train-test-splitting)
### [5. Predictive Modelling](#predictive-modelling)
### [6. Conclusion](#conclusion)
### [7. App Deployment](#app-creation-and-deployment)

# Dataset
* Dataset Imported from kaggle
* The Dataset contains 14 attributes
1. Age : Age of the patient
2. Sex : Sex of the patient
3. cp : Chest Pain type chest pain type
   * Value 1: typical angina
   * Value 2: atypical angina
   * Value 3: non-anginal pain
   * Value 4: asymptomatic
4. trestbps : resting blood pressure (in mm Hg)
5. chol : cholestoral in mg/dl fetched via BMI sensor
6. fbs : (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
7. rest_ecg : resting electrocardiographic results
    * Value 0: normal
    * Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
    * Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
8. thalach : maximum heart rate achieved
9. exang: exercise induced angina (1 = yes; 0 = no)
10. oldpeak: ST depression induced by exercise relative to rest OR Patient's old peak history recorded
11. slope: the slope of the peak exercise ST segment
    * Value 1: upsloping
    * Value 2: flat
    * Value 3: downsloping
12. ca: the number of major blood vessels with a fluorescent color (0-4). Fluorescent color is mainly associated with diabetes
13. thal: Thalassemia
14. target : 0= less chance of heart attack 1= more chance of heart attack


# Data Exploration
- Dataset had 14 features and 303 samples
- Dataset had 5 numerical and 8 categorical features
- Slightly imbalanced dataset with 54.5% diseased patients
- No null value in dataset
- Many outliers present in our dataset

# Data Preprocessing
- 1 duplicate row was present which was removed
- No null value in dataset
- Applied dummy encoding on dataset
- After removal of outliers dataset contained 283 samples

# Train-Test Splitting
- Applied Standard scaler method for scaling (Standardization) 
- Also applied MinMaxScaler but did not used with Application
- Test size was 20% of dataset

# Predictive Modelling
Applied various Machine learning algorithms like-
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Naive Bayes' Classifier
- Support Vector Machine
- K-Nearest Neighbours
- Gradient Boosting
- Extreme Gradient Boosting (XG Boost)

1. Created Confusion matrix for all classifiers
2. Drawn plot of Roc Curves
3. Made Classification report
4. Applied RandomizedSearchCV and RepeatedStratifiedKfold for hyperparameters tuning

# Conclusion
Logistic Regression algorithm worked best for our Dataset providing accuracy of 89.5%

# App Creation and Deployment
- App was created using FLASK - a micro web framework in python
- App was deployed using Heroku - providing platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- App link - https://heart--disease--predictions.herokuapp.com/



### References for developing flask api and html
*   https://www.geeksforgeeks.org/deploy-machine-learning-model-using-flask/   (Full Template)
*   https://www.digitalocean.com/community/tutorials/how-to-use-and-validate-web-forms-with-flask-wtf
*   https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04
*   https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3
*   https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application
*   https://www.digitalocean.com/community/tutorial_series/how-to-build-a-website-with-html
*   https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
