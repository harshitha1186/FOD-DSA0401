from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load Dataset
iris = load_iris()

X = iris.data
y = iris.target

# Train Model
model = DecisionTreeClassifier()
model.fit(X, y)

# User Input
sepal_length = float(input("Enter Sepal Length: "))
sepal_width = float(input("Enter Sepal Width: "))
petal_length = float(input("Enter Petal Length: "))
petal_width = float(input("Enter Petal Width: "))

flower = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]

prediction = model.predict(flower)

species = iris.target_names[prediction[0]]

print("\nPredicted Species:", species)
