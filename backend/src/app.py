from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Resilient Cloud Infrastructure!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "This is a sample API."}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
