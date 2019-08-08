from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
        return "Hello world, welcome from my Flask app"

app.run(host='0.0.0.0', port=80)
