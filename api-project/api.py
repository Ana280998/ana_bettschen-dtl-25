from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
OPENROUTER_TOKEN = os.getenv("OPENROUTER_TOKEN")

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("input")

        if not user_input:
            return jsonify({"error": "Missing 'input' field"}), 400

        headers = {
            "Authorization": f"Bearer {OPENROUTER_TOKEN}",
            "Content-Type": "application/json"
        }

        url = f"{API_BASE_URL}/chat/completions"

        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code != 200:
            return jsonify({"error": f"API Error: {response.text}"}), response.status_code

        result = response.json()
        message = result["choices"][0]["message"]["content"]

        return jsonify({"response": message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
