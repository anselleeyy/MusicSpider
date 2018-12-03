import requests
import json
import os
import code.WangYiYun as WangYiYun

headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Referer': 'https://music.163.com/search',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'music.163.com',
        'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
        'DNT': '1',
        'Pragma': 'no-cache'
    }
base_url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token'


def get_artist_album_list(artist):
    param = '{"total":"True","s":"%s","offset":"0","csrf_token":"nothing","limit":"30","type":"10"}' % (
        artist)
    wyy = WangYiYun.WangYiYun(param)
    data = wyy.get_data()
    print('---------- init class WangYiYun ----------')
    response = requests.post(url=base_url, data=data, headers=headers)
    dir_path = '{}'.format(artist)
    os.mkdir(dir_path)
    path = '{}/{}.json'.format(artist, artist)
    file = open(path, 'w', encoding='utf-8')
    json.dump(response.json(), file, ensure_ascii=False)
    print('---------- artist: %s info got succeed ----------' % artist)
    file.close()


if __name__ == '__main__':
    get_artist_album_list(artist='李荣浩')
