import logging
from flask import Flask, request

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
NAME = "Bharadwaj"

name = None


@app.route('/', methods=['GET'])
async def index():
    app.logger.info("Received GET / request")
    # \n to avoid % escape
    return 'Hello {}\n'.format(NAME), 200


@app.route('/set_name', methods=['POST'])
async def set_name():
    global name
    app.logger.info("Received POST /set_name request")
    try:
        payload = request.get_json()
        new_name = payload["name"]
        app.logger.info(f"Request payload: [name: {new_name}]")
        old_name = name
        app.logger.info(f"Stored name: {old_name}")
        name = new_name
        app.logger.info(f"New name: {name}")
        message = {
            "message": "Name changed!",
            "old_name": old_name,
            "new_name": new_name,
        }
        app.logger.info(f"Response: {message}")
        return message, 201
    except Exception as e:
        app.logger.error(e)
        return {"error": str(e)}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
