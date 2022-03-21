from flask import Flask, request
from gevent import pywsgi
import requests
from requests.packages import urllib3
import urllib3

app = Flask(__name__)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings()

@app.route("/")
def helloworld():
    return "Hello World! xian you."

@app.route('/word-query')
def query_word():
    word = request.args.get('word', default = '*', type = str)
    req = requests.get('https://picdict.youdao.com/search?q=' + word + '&le=en',verify=False)
    # resultContent = json.dumps(req.content)
    resultContent = req.json()
    imageList = resultContent["data"]["pic"]
    if imageList:
        print("图片地址为",imageList[0]["image"])
    # print(req.text)
    return imageList[0]["image"]

if __name__ == "__main__":
    # app.run()
    # server = pywsgi.WSGIServer(('0.0.0.0',8088),app)
    # server.serve_forever()

    app.run(debug=True)