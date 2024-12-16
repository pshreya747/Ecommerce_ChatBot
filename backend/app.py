from flask import Flask, request, jsonify  # type: ignore
from flask_cors import CORS  # type: ignore

app = Flask(__name__)
CORS(app)


PRODUCTS = [
    {"id": 1, "name": "Smartphone", "price": 299},
    {"id": 2, "name": "Laptop", "price": 999},
    {"id": 3, "name": "Tablet", "price": 199},
    {"id": 4, "name": "Smartwatch", "price": 149},
    {"id": 5, "name": "Headphones", "price": 89},
    {"id": 6, "name": "Bluetooth Speaker", "price": 79},
    {"id": 7, "name": "Gaming Console", "price": 399},
    {"id": 8, "name": "Camera", "price": 499},
    {"id": 9, "name": "Desktop PC", "price": 599},
    {"id": 10, "name": "Printer", "price": 129},
    {"id": 11, "name": "Monitor", "price": 179},
    {"id": 12, "name": "Keyboard", "price": 49},
    {"id": 13, "name": "Mouse", "price": 39},
    {"id": 14, "name": "Router", "price": 69},
    {"id": 15, "name": "External Hard Drive", "price": 99},
    {"id": 16, "name": "USB Flash Drive", "price": 19},
    {"id": 17, "name": "Power Bank", "price": 29},
    {"id": 18, "name": "Earbuds", "price": 59},
    {"id": 19, "name": "Fitness Tracker", "price": 129},
    {"id": 20, "name": "E-Reader", "price": 199},
]


GREETINGS = ["hello", "hi", "hey", "good morning", "good evening", "good afternoon"]

@app.route('/api/chat', methods=['POST'])
def chatbot():
    user_message = request.json.get('message', '').lower()


    if any(greeting in user_message for greeting in GREETINGS):
        return jsonify({"reply": "Hi! How can I help you today?"})

   
    for product in PRODUCTS:
        if product['name'].lower() in user_message:
            return jsonify({"reply": f"We have {product['name']}s starting at ${product['price']}!"})

   
    return jsonify({"reply": "Sorry, I didn’t understand that. Please specify a product!"})


if __name__ == '__main__':
    app.run(debug=True)
