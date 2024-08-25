from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'GET':
        # Return the hardcoded operation code
        return jsonify({"operation_code": 1}), 200
    
    if request.method == 'POST':
        data = request.get_json().get('data', [])
        
        user_id = "SATWIK_KRISHNA_02032004"
        email = "satwikkrishna.pv2021@vitstudent.ac.in"
        roll_number = "21BCT0140"
        
        # Initialize empty arrays
        numbers = []
        alphabets = []
        highest_lowercase_alphabet = []

        for item in data:
            if item.isdigit():  # If item is a number
                numbers.append(item)
            elif item.isalpha():  # If item is an alphabet
                alphabets.append(item)
                if item.islower():  # Track the highest lowercase alphabet
                    if not highest_lowercase_alphabet or item > highest_lowercase_alphabet[0]:
                        highest_lowercase_alphabet = [item]

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }

        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)