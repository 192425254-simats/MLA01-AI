import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Age": [25, 30, 35, 28, 45, 40, 23, 50, 32, 38],
    "Income": [25000, 40000, 50000, 30000, 60000,
               45000, 20000, 70000, 35000, 55000],
    "CreditScore": [550, 650, 700, 580, 750,
                    680, 520, 800, 600, 720],
    "ExistingLoan": [1, 0, 0, 1, 0,
                     0, 1, 0, 1, 0],
    "LoanStatus": [0, 1, 1, 0, 1,
                   1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Features
X = df[["Age", "Income", "CreditScore", "ExistingLoan"]]

# Target
y = df["LoanStatus"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create Decision Tree
model = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=3,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Predicted Values:", y_pred)
print("Actual Values:", y_test.values)
print("Accuracy:", accuracy)

# Predict a new customer
new_customer = [[35, 50000, 700, 0]]

prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("Loan Status: APPROVED")
else:
    print("Loan Status: REJECTED")

# Display tree
plt.figure(figsize=(12, 7))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Reject", "Approve"],
    filled=True
)

plt.show()
