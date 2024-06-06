from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Custom unpickler to handle old module paths
class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == 'sklearn.linear_model.logistic':
            module = 'sklearn.linear_model'
        return super().find_class(module, name)

# Load the model using the custom unpickler
with open('model.pkl', 'rb') as f:
    model = CustomUnpickler(f).load()

@app.route('/')
def hello_world():
    return render_template("forest_fire.html")

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model.predict_proba(final)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)

    if float(output) > 0.5:
        return render_template('forest_fire.html', pred='Your Forest is in Danger.\nProbability of fire occurring is {}'.format(output), bhai="Your Forest is in Danger")
    else:
        return render_template('forest_fire.html', pred='Your Forest is safe.\nProbability of fire occurring is {}'.format(output), bhai="Your Forest is Safe for now")

if __name__ == '__main__':
    app.run(debug=True)
