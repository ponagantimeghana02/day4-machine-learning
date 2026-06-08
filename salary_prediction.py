from sklearn.linear_model import LinearRegression
import numpy as np

experience = [1, 2, 3, 5, 7, 10, 12, 15]
salary = [25000, 30000, 35000, 45000, 55000, 70000, 85000, 100000]

X = np.array(experience).reshape(-1, 1)
y = np.array(salary)

model = LinearRegression()
model.fit(X, y)

years = np.array([4, 8, 20]).reshape(-1, 1)
predictions = model.predict(years)

print("Salary Predictions")
print("-" * 30)

for exp, sal in zip([4, 8, 20], predictions):
    print(f"Experience: {exp} years -> Predicted Salary: ₹{sal:.2f}")