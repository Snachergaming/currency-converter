from flask import Flask, render_template, request

app = Flask(__name__)

# Define currencies and their conversion rates
currencies = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.75,
    'INR': 83.96,
    'JPY': 110.0,
    'AUD': 1.35,
    'CAD': 1.25,
    'CHF': 0.92,
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    conversion_rate = None
    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = float(request.form['amount'])

        # Calculate the conversion
        if from_currency in currencies and to_currency in currencies:
            rate = currencies[to_currency] / currencies[from_currency]
            converted_amount = amount * rate
            conversion_rate = rate
            result = f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"
        else:
            result = "Conversion rate not available."

    return render_template('index.html', currencies=currencies, result=result, conversion_rate=conversion_rate)

if __name__ == '__main__':
    app.run(debug=True)
