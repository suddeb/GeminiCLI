# Import necessary libraries
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # For this example, we'll just print the data
        print(f'Name: {name}, Email: {email}, Message: {message}')
        return 'Thank you for your message!'
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
