# AI-Driven Customer Analytics Platform Using Flask

## Overview

The AI-Driven Customer Analytics Platform is a Flask-based web application that helps businesses analyze customer data using Machine Learning techniques. The system provides customer segmentation, churn prediction, purchase prediction, and product recommendations through an interactive dashboard.

---

## Features

### User Authentication

* Login Page
* Registration Page
* Session Management
* Logout Functionality

### Dashboard

* Total Customers
* Active Customers
* Churn Customers
* Premium Customers
* Interactive Charts

### Customer Management

* View Customer Dataset
* Customer Information Table
* Search and Analysis Ready Data

### Customer Segmentation

* K-Means Clustering
* Premium Customers
* Regular Customers
* Low Value Customers

### Churn Prediction

Predicts whether a customer is likely to churn based on:

* Age
* Annual Income
* Purchase Frequency
* Total Spending

### Purchase Prediction

Predicts future customer purchase behavior using Machine Learning.

### Recommendation System

Generates product recommendations based on customer preferences.

### Data Visualization

* Pie Charts
* Doughnut Charts
* Bar Charts
* Line Charts
* Customer Analytics Graphs

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Chart.js

### Backend

* Python
* Flask

### Machine Learning

* Scikit-Learn
* K-Means Clustering

### Data Processing

* Pandas
* NumPy

---

## Project Structure

project/

├── app.py

├── dataset/

│ └── customers.csv

├── models/

│ ├── segmentation.py

│ ├── churn_prediction.py

│ ├── purchase_prediction.py

│ └── recommendation.py

├── templates/

│ ├── login.html

│ ├── register.html

│ ├── dashboard.html

│ ├── customers.html

│ ├── prediction.html

│ └── recommendation.html

├── static/

│ ├── style.css

│ └── chart.js

├── requirements.txt

└── README.md

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## Default Login Credentials

Username:

```text
admin
```

Password:

```text
admin123
```

---

## Dataset Attributes

The application uses a customer dataset containing:

* Customer_ID
* Age
* Gender
* Location
* Annual_Income
* Purchase_Frequency
* Total_Spending
* Membership_Status
* Preferred_Product_Category
* Churn_Status

---

## Machine Learning Modules

### Customer Segmentation

Uses K-Means Clustering to group customers into:

* Premium Customers
* Regular Customers
* Low Value Customers

### Churn Prediction

Predicts customer retention probability.

### Purchase Prediction

Predicts future customer purchasing behavior.

### Recommendation Engine

Suggests products based on customer preferences and purchase patterns.

---

## Future Enhancements

* Real Database Integration
* User Registration Storage
* Advanced Recommendation Algorithms
* Deep Learning Models
* Email Notifications
* Real-Time Analytics Dashboard
* Cloud Deployment

---

## Conclusion

The AI-Driven Customer Analytics Platform demonstrates how Flask and Machine Learning can be combined to analyze customer behavior, predict future actions, and support business decision-making through intelligent analytics and visualization.

---

## Author

Project Developed Using:

* Python
* Flask
* Machine Learning
* Bootstrap
* Chart.js
