from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

def send_email(lat, lon):
    sender = "s.shashttikha@gmail.com"        # <-- your Gmail
    receiver = "24i258@psgtech.ac.in"  # <-- who gets the alert
    password = "adge tdes rgml qnns" # <-- paste App Password here

    message = f"Subject: EMERGENCY ALERT 🚨\n\nUser needs help!\nLocation: {lat}, {lon}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/alert')
def alert():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    print(f"🚨 ALERT! Location: {lat}, {lon}")

    send_email(lat, lon)

    return f"🚨 Alert sent! Location: {lat}, {lon}"

if __name__ == '__main__':
    app.run(debug=True)