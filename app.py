from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('flight_price_predictor.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Extract form data
        airline = int(request.form['airline'])
        flight = int(request.form['flight'])
        source_city = int(request.form['source_city'])
        departure_time = int(request.form['departure_time'])
        stops = int(request.form['stops'])
        arrival_time = int(request.form['arrival_time'])
        destination_city = int(request.form['destination_city'])
        flight_class = int(request.form['class'])
        duration = int(request.form['duration'])
        days_left = int(request.form['days_left'])

        # Make prediction
        features = [[airline, flight, source_city, departure_time, stops, arrival_time, destination_city, flight_class, duration, days_left]]
        predicted_price = model.predict(features)[0]

        return render_template('results.html', price=predicted_price)

    return render_template('predict.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process contact form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        # You can add more logic to process the contact form data
        return "Message sent successfully!"
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
