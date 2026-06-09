from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd

from models.segmentation import customer_segmentation
from models.churn_prediction import churn_prediction
from models.purchase_prediction import purchase_prediction
from models.recommendation import get_recommendations

app = Flask(__name__)
app.secret_key = "customeranalytics"

DATASET = "dataset/customers.csv"


# ---------------------------
# Login Page
# ---------------------------
@app.route("/")
def login():
    return render_template("login.html")


# ---------------------------
# Login Validation
# ---------------------------
@app.route("/login", methods=["POST"])
def login_user():
    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "admin123":
        session["user"] = username
        return redirect(url_for("dashboard"))

    return render_template("login.html", error="Invalid Username or Password")


# ---------------------------
# Register Page
# ---------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return render_template("register.html", error="Passwords do not match")

        return redirect(url_for("login"))

    return render_template("register.html")


# ---------------------------
# Dashboard
# ---------------------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    df = pd.read_csv(DATASET)

    total_customers = len(df)
    active_customers = len(df[df["Churn_Status"] == 0])
    churn_customers = len(df[df["Churn_Status"] == 1])
    premium_customers = len(df[df["Membership_Status"] == "Premium"])

    return render_template(
        "dashboard.html",
        total_customers=total_customers,
        active_customers=active_customers,
        churn_customers=churn_customers,
        premium_customers=premium_customers
    )


# ---------------------------
# Customers Page
# ---------------------------
@app.route("/customers")
def customers():
    if "user" not in session:
        return redirect(url_for("login"))

    df = pd.read_csv(DATASET)
    customers_data = df.to_dict(orient="records")

    return render_template("customers.html", customers=customers_data)


# ---------------------------
# Segmentation
# ---------------------------
@app.route("/segmentation")
def segmentation():
    if "user" not in session:
        return redirect(url_for("login"))

    segmented_data = customer_segmentation()

    return render_template(
        "customers.html",
        customers=segmented_data.to_dict(orient="records")
    )


# ---------------------------
# Prediction Page
# ---------------------------
@app.route("/prediction")
def prediction():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("prediction.html")


# ---------------------------
# Churn Prediction
# ---------------------------
@app.route("/predict_churn", methods=["POST"])
def predict_churn():
    age = int(request.form["age"])
    income = float(request.form["income"])
    frequency = int(request.form["frequency"])
    spending = float(request.form["spending"])

    result = churn_prediction(age, income, frequency, spending)

    customer_data = {
        "customer_id": request.form["customer_id"],
        "age": age,
        "gender": request.form["gender"],
        "location": request.form["location"],
        "income": income,
        "frequency": frequency,
        "spending": spending,
        "membership": request.form["membership"]
    }

    return render_template(
        "prediction.html",
        churn_result=result,
        customer_data=customer_data
    )


# ---------------------------
# Purchase Prediction
# ---------------------------
@app.route("/predict_purchase", methods=["POST"])
def predict_purchase():
    age = int(request.form["age"])
    income = float(request.form["income"])
    frequency = int(request.form["frequency"])
    spending = float(request.form["spending"])

    result = purchase_prediction(age, income, frequency, spending)

    customer_data = {
        "customer_id": request.form["customer_id"],
        "age": age,
        "gender": request.form["gender"],
        "location": request.form["location"],
        "income": income,
        "frequency": frequency,
        "spending": spending,
        "membership": request.form["membership"]
    }

    return render_template(
        "prediction.html",
        purchase_result=result,
        customer_data=customer_data
    )


# ---------------------------
# Recommendation
# ---------------------------
@app.route("/recommendation")
def recommendation():
    if "user" not in session:
        return redirect(url_for("login"))

    recommendations = get_recommendations()

    return render_template(
        "recommendation.html",
        recommendations=recommendations
    )


# ---------------------------
# Logout
# ---------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
