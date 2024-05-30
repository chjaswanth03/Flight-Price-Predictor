import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Sample data generation
data = {
    'airline': [1, 2, 3, 4, 5, 6, 7, 8],
    'flight': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'source_city': [1, 2, 3, 4, 5, 6, 7, 8],
    'departure_time': [1, 2, 3, 4, 5, 6, 7, 8],
    'stops': [0, 1, 0, 1, 0, 1, 0, 1],
    'arrival_time': [1, 2, 3, 4, 5, 6, 7, 8],
    'destination_city': [1, 2, 3, 4, 5, 6, 7, 8],
    'class': [1, 0, 1, 0, 1, 0, 1, 0],
    'duration': [100, 200, 300, 400, 500, 600, 700, 800],
    'days_left': [30, 20, 10, 40, 50, 60, 70, 80],
    'price': [300, 400, 500, 600, 700, 800, 900, 1000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define features and target
X = df.drop('price', axis=1)
y = df['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model to a file
joblib.dump(model, 'flight_price_predictor.pkl')

print("Model has been trained and saved as flight_price_predictor.pkl")
