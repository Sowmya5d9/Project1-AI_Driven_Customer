import pandas as pd
from sklearn.cluster import KMeans


def customer_segmentation():

    # Load Dataset
    df = pd.read_csv("dataset/customers.csv")

    # Features for Clustering
    X = df[
        [
            "Annual_Income",
            "Purchase_Frequency",
            "Total_Spending"
        ]
    ]

    # K-Means Clustering
    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    df["Segment"] = kmeans.fit_predict(X)

    # Rename Segments
    segment_names = {
        0: "Premium Customers",
        1: "Regular Customers",
        2: "Low Value Customers"
    }

    df["Segment"] = df["Segment"].map(segment_names)

    return df


# Run independently for testing
if __name__ == "__main__":

    segmented_df = customer_segmentation()

    print(
        segmented_df[
            [
                "Customer_ID",
                "Annual_Income",
                "Purchase_Frequency",
                "Total_Spending",
                "Segment"
            ]
        ].head()
    )