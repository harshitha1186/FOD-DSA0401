import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder

# CSV file path
file_path = r"C:\Users\harsh\Downloads\28.CSV"

# Read CSV
df = pd.read_csv(file_path)

print("\n========== CAR DATA ==========")
print(df)

print("\nAvailable columns:")
print(df.columns.tolist())

# Create encoders
brand_encoder = LabelEncoder()
engine_encoder = LabelEncoder()

# Encode categorical columns
df['Brand'] = brand_encoder.fit_transform(df['Brand'])
df['Engine'] = engine_encoder.fit_transform(df['Engine'])

# Features
X = df[['Mileage', 'Age', 'Brand', 'Engine']]

# Target
y = df['Price']

# Create CART model
model = DecisionTreeRegressor(random_state=42)

# Train model
model.fit(X, y)

print("\nCART model trained successfully.")

# User input
print("\n========== ENTER NEW CAR DETAILS ==========")

mileage = float(input("Enter Mileage: "))
age = float(input("Enter Age of Car: "))

print("\nAvailable Brands:")
print(list(brand_encoder.classes_))

brand_input = input("Enter Brand: ")

print("\nAvailable Engines:")
print(list(engine_encoder.classes_))

engine_input = input("Enter Engine Type: ")

# Encode user input
brand_encoded = brand_encoder.transform([brand_input])[0]
engine_encoded = engine_encoder.transform([engine_input])[0]

# Create new car
new_car = pd.DataFrame(
    [[mileage, age, brand_encoded, engine_encoded]],
    columns=['Mileage', 'Age', 'Brand', 'Engine']
)

# Prediction
predicted_price = model.predict(new_car)[0]

print("\n========== RESULT ==========")
print("Predicted Car Price: ₹", round(predicted_price, 2))

# Decision path
decision_path = model.decision_path(new_car)
leaf_id = model.apply(new_car)[0]

print("\n========== DECISION PATH ==========")

tree = model.tree_
feature_names = X.columns

for node_id in decision_path.indices:

    if node_id == leaf_id:
        print("Reached final leaf node.")
        continue

    feature_index = tree.feature[node_id]

    if feature_index >= 0:

        feature_name = feature_names[feature_index]
        threshold = tree.threshold[node_id]

        value = new_car.iloc[0, feature_index]

        if value <= threshold:
            print(
                f"{feature_name} = {value:.2f} <= "
                f"{threshold:.2f}"
            )
        else:
            print(
                f"{feature_name} = {value:.2f} > "
                f"{threshold:.2f}"
            )
