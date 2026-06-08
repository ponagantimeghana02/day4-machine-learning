from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

experience = [1, 2, 3, 5, 7, 10, 12, 15]
salary = [25000, 30000, 35000, 45000, 55000, 70000, 85000, 100000]

X = np.array(experience).reshape(-1, 1)
y = np.array(salary)

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

report = f"""
MODEL EVALUATION REPORT
=======================

Mean Absolute Error (MAE): {mae:.2f}

Mean Squared Error (MSE): {mse:.2f}

R² Score: {r2:.4f}

Explanation:
------------
1. MAE (Mean Absolute Error)
   - Measures the average prediction error.
   - Lower MAE indicates better model performance.

2. MSE (Mean Squared Error)
   - Measures the average squared difference between
     actual and predicted values.
   - Lower MSE indicates fewer large prediction errors.

3. R² Score
   - Measures how well the model explains the variance
     in the data.
   - R² = 1 means perfect prediction.
   - R² = 0 means the model explains none of the variance.

Model Assessment:
The R² score is very close to 1, indicating that the
linear regression model fits the salary data extremely well.
The low MAE and MSE values show that prediction errors are small.
"""

with open("model_evaluation.txt", "w") as file:
    file.write(report)

print(report)
print("\nReport saved as model_evaluation.txt")