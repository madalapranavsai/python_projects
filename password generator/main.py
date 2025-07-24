
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_password():
    data = request.get_json()
    nr_letters = int(data.get('letters', 4))
    nr_symbols = int(data.get('symbols', 2))
    nr_numbers = int(data.get('numbers', 2))
    
    password_list = []
    
    # Add letters
    for _ in range(nr_letters):
        password_list.append(random.choice(letters))
    
    # Add symbols
    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))
    
    # Add numbers
    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))
    
    # Shuffle the list
    random.shuffle(password_list)
    
    # Convert to string
    password = ''.join(password_list)
    
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

