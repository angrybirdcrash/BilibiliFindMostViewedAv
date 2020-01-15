import requests
import json


def getAvInfo(av):
    getAvInfoUrl = 'https://api.bilibili.com/x/web-interface/view?aid='
    return json.loads(requests.get(getAvInfoUrl + av).text)

if __name__ == '__main__':
    print(getAvInfo('22836761'))
