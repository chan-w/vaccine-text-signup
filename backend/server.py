from flask import Flask, request, Response, jsonify, redirect, render_template
#  flask_cors import CORS
app = Flask(__name__)

# CORS(app)

@app.route("/", methods=['GET', 'POST'])
def landing():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=4000,
        debug=True
    )