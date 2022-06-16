# 1. Save this file as `app.py`
# 2. Make sure you have flask installed `pip install flask`
# 3. Run using `flask run -h localhost -p 5000`

from flask import Flask, request

app = Flask(__name__)
name = "Bharadwaj"

@app.route('/', methods=['GET'])
def index():
    return 'Hello {}'.format(name), 200

@app.route('/set_name', methods=['POST'])
def set_name():
    global name
    try:
        payload = request.get_json()
        new_name = payload["name"]
        message = {
            "message": "Name changed!",
            "old_name": name,
            "new_name": new_name,
        }
        name = new_name
        return message, 201
    except Exception as e:
        return {"error": str(e)}, 500