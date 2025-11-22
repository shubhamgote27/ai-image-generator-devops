from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://ai.backtonep.workers.dev/?prompt="

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form.get("prompt")

    try:
        res = requests.get(API_URL + prompt, timeout=60)
        data = res.json()

        if data.get("success"):
            image_url = data["data"]["image_link"]
            return jsonify({"success": True, "image": image_url})
        else:
            return jsonify({"success": False, "error": "API returned failure"})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
