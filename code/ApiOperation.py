import requests
import json
import os
from code.NetEase import NetEase
from code import Commons


class Api:
    @staticmethod
    def get_artist_album_list(artist):
        post_data = '{"total":"True","s":"%s","offset":"0","csrf_token":"nothing","limit":"30","type":"10"}' % artist
        wyy = NetEase(post_data)
        data = wyy.get_data()
        print('---------- init class WangYiYun ----------')
        response = requests.post(url=Commons.search_url, data=data, headers=Commons.headers)
        dir_path = Commons.dir_root + '{}'.format(artist)
        os.mkdir(dir_path)
        path = Commons.dir_root + '{}/{}.json'.format(artist, artist)
        file = open(path, 'w', encoding='utf-8')
        json.dump(response.json(), file, ensure_ascii=False)
        print('---------- artist: %s info got succeed ----------' % artist)
        file.close()
        return

    @staticmethod
    def get_album_info(album_id):
        url = Commons.album_url + str(album_id)
        response = requests.get(url=url, headers=Commons.headers)
        print(response.json())
        return response


def read_file(filename, artist):
    file = open(file=filename, mode='r', encoding='utf-8')
    s = json.load(file)
    album_count = s['result']['albumCount']
    for i in range(album_count):
        album_name = s['result']['albums'][i]['name']
        dir_path = Commons.dir_root + '{}/{}/'.format(artist, album_name)
        os.mkdir(dir_path)
        json_file = dir_path + '{}.json'.format(album_name)
        file = open(file=json_file, mode='w', encoding='utf-8')
        api = Api()
        response = api.get_album_info(album_id=s['result']['albums'][i]['id'])
        json.dump(response.json(), file, ensure_ascii=False)
        file.close()


if __name__ == '__main__':
    param = '李荣浩'
    # api = Api()
    # api.get_artist_album_list(artist=param)
    file_name = Commons.dir_root + '{}/{}.json'.format(param, param)
    read_file(filename=file_name, artist=param)
