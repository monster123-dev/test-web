from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Process the form data (e.g., save to a database, send an email, etc.)
    return f"Thank you, {name}! Your message has been received."

if __name__ == "__main__":
    app.run(debug=True)
