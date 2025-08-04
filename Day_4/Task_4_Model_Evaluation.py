# Task 4: Model Evaluation (R2 Score)

from sklearn.metrics import r2_score

# Actual vs Predicted
r2 = r2_score(y, y_pred)
print("R2 Score:", r2)

📌 A higher R² score means a better fit. R² = 1 is perfect prediction.
