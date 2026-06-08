import pandas as pd

# Dataset
employees = {
    "age": [22, 25, 28, None, 35, 40, None, 29],
    "salary": [25000, 30000, None, 45000, 50000, 70000, 38000, None],
    "experience": [1, 2, 3, 5, None, 12, 2, 4]
}

df = pd.DataFrame(employees)

missing_values = df.isnull().sum()

df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].mean())
df["experience"] = df["experience"].fillna(df["experience"].mean())


invalid_age = df[df["age"] < 0]
invalid_salary = df[df["salary"] < 0]
invalid_experience = df[df["experience"] < 0]


report = []

report.append("DATA PREPROCESSING REPORT")
report.append("=" * 40)

report.append("\n1. Missing Values Detected:")
report.append(str(missing_values))

report.append("\n2. Missing Values Filled Using Mean")
report.append("\nUpdated Dataset:")
report.append(df.to_string())

report.append("\n\n3. Data Validation Results:")

if len(invalid_age) == 0:
    report.append("\nNo invalid age values found.")
else:
    report.append("\nInvalid age values detected.")

if len(invalid_salary) == 0:
    report.append("No invalid salary values found.")
else:
    report.append("Invalid salary values detected.")

if len(invalid_experience) == 0:
    report.append("No invalid experience values found.")
else:
    report.append("Invalid experience values detected.")

# Save report
with open("preprocessing_report.txt", "w") as file:
    file.write("\n".join(report))

print("Preprocessing completed successfully!")
print("Report saved as preprocessing_report.txt")