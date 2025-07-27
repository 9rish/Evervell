from flask import Flask, request, jsonify
from main import main  # Import your main function

app = Flask(__name__)

# Add a route to check if the server is running
@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.json  # Make sure you're sending JSON
    language = data.get('language')
    gender = data.get('gender')
    age = data.get('age')

    # Call the main function and get the response
    response = main(language, gender, age)  

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
