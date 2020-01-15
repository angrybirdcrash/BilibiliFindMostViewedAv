import requests
import json


def getAvInfo(av):
    # getAvInfoUrl = 'https://api.bilibili.com/x/web-interface/view?aid='
    getAvInfoUrl = 'http://api.bilibili.com/archive_stat/stat?aid='
    return json.loads(requests.get(getAvInfoUrl + str(av)).text)


if __name__ == '__main__':
    maxView = 0
    for av in range(1, 90000000):
        print(av)
        avInfo = getAvInfo(av)
        if avInfo['code'] == 0:
            # view = avInfo['data']['stat']['view']
            # print('max = ' + str(maxView) + ', ' + avInfo['data']['title'] + ' ' + str(view))
            view = avInfo['data']['view']
            if view == '--':
                continue
            print('max = ' + str(maxView) + ', ' + ' ' + str(view))
            if view > maxView:
                maxView = view
