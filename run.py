import requests
import json


# http://api.bilibili.com/archive_stat/stat?aid=8614334
def getAvInfo(av):
    getAvInfoUrl = 'https://api.bilibili.com/x/web-interface/view?aid='
    return json.loads(requests.get(getAvInfoUrl + str(av)).text)


if __name__ == '__main__':
    maxView = 0
    for av in range(1, 90000000):
        print(av)
        avInfo = getAvInfo(av)
        if avInfo['code'] == 0:
            view = avInfo['data']['stat']['view']
            print('max = ' + str(maxView) + ', ' + avInfo['data']['title'] + ' ' + str(view))
            if view > maxView:
                maxView = view
