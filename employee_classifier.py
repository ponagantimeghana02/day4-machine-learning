from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Dataset
experience = [1, 2, 3, 5, 7, 10, 12, 15]

status = [
    "Junior",
    "Junior",
    "Junior",
    "Mid",
    "Mid",
    "Senior",
    "Senior",
    "Senior"
]

X = np.array(experience).reshape(-1, 1)
y = np.array(status)

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

test_experience = np.array([4, 8, 13]).reshape(-1, 1)
predictions = model.predict(test_experience)

print("Employee Category Predictions")
print("=" * 35)

for exp, category in zip([4, 8, 13], predictions):
    print(f"Experience: {exp} years -> Category: {category}")