from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("models/gemini-flash-latest")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    print("🔥 /chat HIT")   # DEBUG

    data = request.json
    user_message = data["message"]

    response = model.generate_content(user_message)

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)
