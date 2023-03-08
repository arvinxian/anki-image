from flask import Flask, request
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
    return resultContent
    
    # imageList = resultContent["data"]["pic"]
    # if imageList:
    #     print("图片地址为",imageList[0]["image"])
    # # print(req.text)
    # return imageList[0]["image"]

@app.route('/sentence-query')
def query_sentence():
    word = request.args.get('word', default = '*', type = str)
    # req = requests.get('https://picdict.youdao.com/search?q=' + word + '&le=en',verify=False)
    # resultContent = json.dumps(req.content)
    # resultContent = req.json()
    
    
    url = "https://dict.youdao.com/jsonapi_s?doctype=json"

    payload='q=' + word
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    # 'Cookie': 'OUTFOX_SEARCH_USER_ID=1823179802@120.235.177.185'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response.text

if __name__ == "__main__":
    # app.run()
    # server = pywsgi.WSGIServer(('0.0.0.0',8088),app)
    # server.serve_forever()

    app.run(debug=True)