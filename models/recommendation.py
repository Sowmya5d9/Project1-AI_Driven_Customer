import pandas as pd

def get_recommendations():

    df = pd.read_csv("dataset/customers.csv")

    category_count = (
        df["Preferred_Product_Category"]
        .value_counts()
        .reset_index()
    )

    category_count.columns = ["Category", "Customers"]

    recommendations = []

    # LOOP MULTIPLE TIMES to reach 20
    while len(recommendations) < 20:
        for _, row in category_count.iterrows():

            recommendations.append({
                "category": row["Category"],
                "customers": row["Customers"],
                "recommendation": f"Recommend more products from {row['Category']}"
            })

            if len(recommendations) == 20:
                break

    return recommendations


# Testing
if __name__ == "__main__":

    recommendations = get_recommendations()

    for item in recommendations:
        print(item)