from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved model file
with open('models/customer_kmeans_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Simple text descriptions for our 5 clusters
cluster_names = {
    0: "Standard Class (Average Income, Average Spend)",
    1: "High-Value Target (High Income, High Spend)",
    2: "Careless Spender (Low Income, High Spend)",
    3: "Careful Saver (High Income, Low Spend)",
    4: "Sensible Shopper (Low Income, Low Spend)"
}

@app.route('/')
def home():
    # Just show the main HTML page
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Grab the inputs from the HTML boxes
    income_input = float(request.form['income'])
    spending_input = float(request.form['spending'])
    
    # Put inputs into the 2D array format the model expects
    user_data = np.array([[income_input, spending_input]])
    
    # Predict the cluster number (0, 1, 2, 3, or 4)
    prediction = model.predict(user_data)
    cluster_number = int(prediction[0])
    
    # Get the text name for that cluster number
    result_text = cluster_names[cluster_number]
    
    # Send the result back to the HTML page
    return render_template('index.html', result=result_text)

if __name__ == '__main__':
    app.run(debug=True)
    