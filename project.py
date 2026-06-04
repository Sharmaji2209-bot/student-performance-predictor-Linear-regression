import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# ---------------------------------------------------------------------
# Task 1: Create Dataset
# ---------------------------------------------------------------------
study_data = {
    'Study_Hours': [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5],
    'Exam_Score': [30, 40, 46, 50, 58, 65, 72, 80, 85, 92]
}

df = pd.DataFrame(study_data)

print("Dataset:")
print(df)

# -----------------------------------------------------------------------
# Task 2: Prepare Data & Train Model
# -----------------------------------------------------------------------
X = df[['Study_Hours']]
y = df['Exam_Score']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# ------------------------------------------------------------------------
# Task 3: Prediction & Evaluation
# ------------------------------------------------------------------------
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
print(f"\nMean Absolute Error: {mae:.2f}")

results = pd.DataFrame({
    'Actual': y_test,
    'Predicted': y_pred
})
print("\nActual vs Predicted:")
print(results)

# Predict new value
new_hours = [[4.5]]
predicted_score = model.predict(new_hours)
print(f"\nPredicted score for 4.5 hours: {predicted_score[0]:.2f}")

# -----------------------------------------------------------------
# Graph (Visualization)
# -----------------------------------------------------------------
plt.scatter(X, y)
plt.plot(X, model.predict(X))

plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score")

plt.show()
