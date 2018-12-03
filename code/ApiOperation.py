import requests
import json
import os
from code.WangYiYun import WangYiYun
from code import Commons

base_url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token'


def get_artist_album_list(artist):
    param = '{"total":"True","s":"%s","offset":"0","csrf_token":"nothing","limit":"30","type":"10"}' % (
        artist)
    wyy = WangYiYun(param)
    data = wyy.get_data()
    print('---------- init class WangYiYun ----------')
    response = requests.post(url=base_url, data=data, headers=Commons.headers)
    dir_path = Commons.dir_root + '{}'.format(artist)
    os.mkdir(dir_path)
    path = Commons.dir_root + '{}/{}.json'.format(artist, artist)
    file = open(path, 'w', encoding='utf-8')
    json.dump(response.json(), file, ensure_ascii=False)
    print('---------- artist: %s info got succeed ----------' % artist)
    file.close()


if __name__ == '__main__':
    get_artist_album_list(artist='李荣浩')
