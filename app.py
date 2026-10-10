
from pathlib import Path

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={
    r"/save": {
        "origins": [
            "http://localhost:5500",
            "http://127.0.0.1:5500"
        ]
    }
})

DATA_FILE = Path(__file__).with_name("data.txt")


@app.route("/save", methods=["POST"])
def save_text():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Неверный формат данных"}), 400

    text = data.get("text")

    if not isinstance(text, str) or not text.strip():
        return jsonify({"error": "Введите текст"}), 400

    with open(DATA_FILE, "a", encoding="utf-8") as file:
        file.write(text.strip() + "\n")

    return jsonify({"message": "Текст успешно сохранён"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
