from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'your_smtp_server'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_smtp_username'
app.config['MAIL_PASSWORD'] = 'your_smtp_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message(subject="New message from {}".format(name),
                  recipients=["recipient@example.com"])
    msg.body = "Name: {}\nEmail: {}\n\n{}".format(name, email, message)

    try:
        mail.send(msg)
        return "Email sent successfully!", 200
    except Exception as e:
        print("Error sending email:", str(e))
        return "Failed to send email.", 500

if __name__ == '__main__':
    app.run(debug=True)
