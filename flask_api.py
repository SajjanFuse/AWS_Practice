from flask import Flask, request, jsonify
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# wine dataset for prediction
wine = load_wine()
X, y = wine.data, wine.target

# Decision Tree
clf = DecisionTreeClassifier()
clf.fit(X, y)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    predictions = []

    for _ in range(2):  # Generate random data for 2 wines
        # Generate random data for wine
        data = np.random.rand(1, 13) * np.array([15, 5, 5, 30, 200, 5, 5, 2, 5, 10, 2, 5, 1500])
        
        prediction = clf.predict(data)

        class_idx = int(prediction[0])
        class_name = wine.target_names[class_idx]
        class_desc = wine.DESCR.split('\n\n')[1].split('\n')[class_idx].strip()

        features = {
            'alcohol': data[0][0],
            'malic_acid': data[0][1],
            'ash': data[0][2],
            'alcalinity_of_ash': data[0][3],
            'magnesium': data[0][4],
            'total_phenols': data[0][5],
            'flavanoids': data[0][6],
            'nonflavanoid_phenols': data[0][7],
            'proanthocyanins': data[0][8],
            'color_intensity': data[0][9],
            'hue': data[0][10],
            'od280/od315_of_diluted_wines': data[0][11],
            'proline': data[0][12]
        }

        predictions.append({
            'predicted_class': class_name,
            'class_description': class_desc,
            'sample_features': features
        })

    return jsonify(predictions)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)