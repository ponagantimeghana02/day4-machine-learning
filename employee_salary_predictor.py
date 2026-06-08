import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Dataset
experience = [1, 2, 3, 5, 7, 10, 12, 15]
salary = [25000, 30000, 35000, 45000, 55000, 70000, 85000, 100000]

X = np.array(experience).reshape(-1, 1)
y = np.array(salary)

model = LinearRegression()
is_trained = False

predictions_history = []


def train_model():
    global is_trained
    model.fit(X, y)
    is_trained = True
    print("\n✅ Model trained successfully!")


def predict_salary():
    if not is_trained:
        print("\n❌ Please train the model first.")
        return

    exp = float(input("Enter years of experience: "))
    predicted_salary = model.predict([[exp]])[0]

    print(f"Predicted Salary: ₹{predicted_salary:.2f}")

    predictions_history.append({
        "Experience": exp,
        "Predicted Salary": round(predicted_salary, 2)
    })


def evaluate_model():
    if not is_trained:
        print("\n❌ Please train the model first.")
        return

    y_pred = model.predict(X)

    mae = mean_absolute_error(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    print("\n===== MODEL EVALUATION =====")
    print(f"MAE : {mae:.2f}")
    print(f"MSE : {mse:.2f}")
    print(f"R² Score : {r2:.4f}")

    if r2 > 0.90:
        print("Excellent model performance!")
    elif r2 > 0.75:
        print("Good model performance.")
    else:
        print("Model needs improvement.")


def export_predictions():
    if len(predictions_history) == 0:
        print("\n❌ No predictions available to export.")
        return

    df = pd.DataFrame(predictions_history)
    df.to_csv("salary_predictions.csv", index=False)

    print("\n✅ Predictions exported to salary_predictions.csv")


while True:
    print("\n===== EMPLOYEE SALARY PREDICTOR =====")
    print("1. Train Model")
    print("2. Predict Salary")
    print("3. Evaluate Model")
    print("4. Export Predictions")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        train_model()

    elif choice == "2":
        predict_salary()

    elif choice == "3":
        evaluate_model()

    elif choice == "4":
        export_predictions()

    elif choice == "5":
        print("\nThank you for using Employee Salary Predictor!")
        break

    else:
        print("\n❌ Invalid choice. Please try again.") 