import pandas as pd
from sklearn.linear_model import LogisticRegression


def churn_prediction(age, income, frequency, spending):

    # Load Dataset
    df = pd.read_csv("dataset/customers.csv")

    # Features
    X = df[
        [
            "Age",
            "Annual_Income",
            "Purchase_Frequency",
            "Total_Spending"
        ]
    ]

    # Target
    y = df["Churn_Status"]

    # Train Model
    model = LogisticRegression(max_iter=1000)

    model.fit(X, y)

    # Predict
    prediction = model.predict(
        [[
            age,
            income,
            frequency,
            spending
        ]]
    )

    if prediction[0] == 1:
        return "Customer is likely to Churn"
    else:
        return "Customer is likely to Stay"


# Testing
if __name__ == "__main__":

    result = churn_prediction(
        30,      # Age
        50000,   # Annual Income
        12,      # Purchase Frequency
        25000    # Total Spending
    )

    print(result)