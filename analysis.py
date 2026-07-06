import pandas as pd
import matplotlib.pyplot as plt

# Load student performance data
df = pd.read_csv("data.csv")

# Basic statistics
average_score = df["score"].mean()
average_attendance = df["attendance"].mean()

print("Average Score:", average_score)
print("Average Attendance:", average_attendance)

# Identify at-risk students
at_risk = df[df["score"] < 60]
print("\nAt-risk students:")
print(at_risk)

# Group students by performance level
def performance_level(score):
    if score >= 85:
        return "High"
    elif score >= 70:
        return "Medium"
    else:
        return "Low"

df["performance_level"] = df["score"].apply(performance_level)

print("\nPerformance distribution:")
print(df["performance_level"].value_counts())

# Create visualization
df["performance_level"].value_counts().plot(kind="bar")
plt.title("Student Performance Distribution")
plt.xlabel("Performance Level")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("results.png")
plt.show()