
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Load the dataset
data = pd.read_csv("love_life_dataset.csv")

# 2. Select input features
features = [
    "trust",
    "understanding",
    "communication",
    "care",
    "support",
    "memories"
]

X = data[features]
y = data["love_score"]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 4. Create the model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# 5. Train the model
model.fit(X_train, y_train)

# 6. Evaluate the model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("❤️ Love Life Model Training Complete!")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.2f}")

# 7. Save the trained model
with open("love_life_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("💕 Model saved as love_life_model.pkl")
