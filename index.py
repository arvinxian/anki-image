from flask import Flask
from gevent import pywsgi

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World! xian you."

if __name__ == "__main__":
    # app.run()
    # server = pywsgi.WSGIServer(('0.0.0.0',8088),app)
    # server.serve_forever()

    app.run(debug=True)