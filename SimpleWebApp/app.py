from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Here you can add code to process the form data, such as sending an email or saving to a database
    print(f'Name: {name}, Email: {email}, Message: {message}')
    return 'Form submitted successfully!' 

if __name__ == '__main__':
    app.run(debug=True)