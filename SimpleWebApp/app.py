"""
This is a simple Flask web application with three routes:
- /: Renders the index page.
- /about: Renders the about page.
- /contact: Renders the contact page and handles form submissions.
"""
# Import necessary libraries which include Flask and render_template
from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    """Renders the index page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Renders the contact page and handles form submissions."""
    if request.method == 'POST':
        # Handle form submission
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # For this example, we'll just print the data
        print(f'Name: {name}, Email: {email}, Message: {message}')
        return 'Thank you for your message!'
    return render_template('contact.html')

# Start the development server
if __name__ == '__main__':
    app.run(debug=True)
