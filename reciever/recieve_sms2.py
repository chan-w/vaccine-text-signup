from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_logic():
    # Increment the counter
    counter = session.get('counter', 0)
    counter += 1

    # Save the new counter value in the session
    session['counter'] = counter

    resp = MessagingResponse()

    if counter == 1:
        resp.message('Hi! Please enter your name')
    else:
        body = request.values.get('Body', 'Friend')
        resp.message('Thanks {}!'.format(body))

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
