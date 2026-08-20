#30.Scenario: K-Nearest Neighbors (KNN) Classifier 
You are working on a classification problem to predict whether a patient has a certain medical condition or not based on their symptoms. You have collected a dataset of patients with labelled data  (0 for no condition, 1 for the condition) and various symptom features. 
Write a Python program that allows the user to input the features of a new patient and the value of  k(number of neighbors). The program should use the KNN classifier from the scikit-learn library to predict whether the patient has the medical condition or not based on the input features. 


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# CSV file path
file_path = r"C:\Users\harsh\Downloads\30.CSV"

# Read CSV
df = pd.read_csv(file_path)

print("\n========== PATIENT DATA ==========")
print(df)

print("\nColumns in CSV:")
print(df.columns.tolist())

# Features
features = ['Age', 'Fever', 'Cough', 'Fatigue', 'Headache']

X = df[features]
y = df['Condition']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Get new patient details
print("\n========== NEW PATIENT ==========")

age = float(input("Enter Age: "))
fever = int(input("Fever (0=No, 1=Yes): "))
cough = int(input("Cough (0=No, 1=Yes): "))
fatigue = int(input("Fatigue (0=No, 1=Yes): "))
headache = int(input("Headache (0=No, 1=Yes): "))

# Get k
k = int(input("Enter value of k: "))

# Validate k
if k <= 0 or k > len(df):
    print("Invalid k value.")
    exit()

# New patient
new_patient = [[
    age,
    fever,
    cough,
    fatigue,
    headache
]]

# Scale new patient
new_patient_scaled = scaler.transform(new_patient)

# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors=k)

# Train
knn.fit(X_scaled, y)

# Predict
prediction = knn.predict(new_patient_scaled)[0]

# Probability
probability = knn.predict_proba(new_patient_scaled)[0]

# Nearest neighbors
distances, indices = knn.kneighbors(new_patient_scaled)

print("\n========== KNN RESULT ==========")

print("K value:", k)

if prediction == 1:
    print("Prediction: Patient HAS the medical condition.")
else:
    print("Prediction: Patient DOES NOT HAVE the medical condition.")

print("\nProbability:")
print("No Condition:", round(probability[0] * 100, 2), "%")
print("Condition:", round(probability[1] * 100, 2), "%")

print("\n========== NEAREST NEIGHBORS ==========")

for i in range(k):
    index = indices[0][i]

    print(
        "Neighbor", i + 1,
        "| Distance:", round(distances[0][i], 4),
        "| Condition:", df.iloc[index]['Condition']
    )
