import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

experience = [1, 2, 3, 5, 7, 10, 12, 15]
salary = [25000, 30000, 35000, 45000, 55000, 70000, 85000, 100000]

X = np.array(experience).reshape(-1, 1)
y = np.array(salary)

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

plt.figure(figsize=(8, 5))

plt.scatter(experience, salary, label="Actual Salary")

plt.plot(experience, y_pred, label="Regression Line")

plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)

plt.savefig("salary_regression.png")

plt.show()

print("Visualization saved as 'salary_regression.png'")