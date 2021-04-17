from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

SECRET_KEY = "password123"

app = Flask(__name__)
app.config.from_object(__name__)

callers = {
    "+19155034543": "Jay",
}

@app.route("/", methods=['GET', 'POST'])
def hello():


    
    counter = session.get('counter', 0)
    counter += 1

    session['counter'] = counter

    from_number = request.values.get('From')
    if from_number in callers:
        name = callers[from_number]
    else:
        name = "Friend"

    message = '{} has messaged {} {} times.' \
        .format(name, request.values.get('To'), counter)

    resp = MessagingResponse()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
