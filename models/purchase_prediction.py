import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def purchase_prediction(age, income, frequency, spending):

    # Load Dataset
    df = pd.read_csv("dataset/customers.csv")

    # Create Purchase Label
    # 1 = Likely Buyer
    # 0 = Not Likely Buyer
    df["Purchase_Label"] = (
        df["Purchase_Frequency"] > 10
    ).astype(int)

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
    y = df["Purchase_Label"]

    # Train Model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

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
        return "Customer is likely to Purchase"
    else:
        return "Customer is not likely to Purchase"


# Testing
if __name__ == "__main__":

    result = purchase_prediction(
        28,      # Age
        60000,   # Income
        15,      # Purchase Frequency
        30000    # Total Spending
    )

    print(result)