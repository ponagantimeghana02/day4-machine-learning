import pandas as pd

employees = {
    "salary": [25000, 30000, 45000, 50000, 70000],
    "experience": [1, 2, 5, 7, 12]
}

df = pd.DataFrame(employees)

def salary_category(salary):
    if salary < 40000:
        return "Low"
    elif salary <= 60000:
        return "Medium"
    else:
        return "High"

def experience_category(exp):
    if exp <= 2:
        return "Junior"
    elif exp <= 7:
        return "Mid"
    else:
        return "Senior"

df["Salary_Category"] = df["salary"].apply(salary_category)
df["Experience_Category"] = df["experience"].apply(experience_category)

print("Employee Dataset with Engineered Features:\n")
print(df)

df.to_csv("employees_feature_engineered.csv", index=False)

print("\nDataset exported successfully as 'employees_feature_engineered.csv'")