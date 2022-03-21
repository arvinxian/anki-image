import json
import requests
from requests.packages import urllib3
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings()
# word = 'devil'
word = input("Enter your word:\n ")
req = requests.get('https://picdict.youdao.com/search?q=' + word + '&le=en',verify=False)
# resultContent = json.dumps(req.content)
resultContent = req.json()
imageList = resultContent["data"]["pic"]
if imageList:
    print("图片地址为",imageList[0]["image"])
# print(req.text)

