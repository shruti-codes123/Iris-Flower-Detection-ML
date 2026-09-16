from flask import Flask, render_template, request
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load Iris Dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create Random Forest Model
model = RandomForestClassifier(
    n_estimators=150,
    max_depth=2,
    min_samples_split=2,
    random_state=42
)

# Train Model
model.fit(X, y)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    probabilities = None

    if request.method == "POST":

        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        flower = [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]]

        # Predict class
        result = model.predict(flower)[0]

        # Get probabilities
        probability_values = model.predict_proba(flower)[0]

        prediction = iris.target_names[result].capitalize()
        confidence = round(probability_values[result] * 100, 2)

        probabilities = {
            "Setosa": round(probability_values[0] * 100, 2),
            "Versicolor": round(probability_values[1] * 100, 2),
            "Virginica": round(probability_values[2] * 100, 2)
        }

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        probabilities=probabilities
    )


if __name__ == "__main__":
    app.run(debug=True)