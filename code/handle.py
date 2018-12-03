import json
import requests
import os
import time
from urllib import request

base_url = 'http://music.163.com/api/album/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Referer': 'http://music.163.com',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'music.163.com',
    'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
    'DNT': '1',
    'Pragma': 'no-cache'
}
cookies = dict(appver='1.2.1', os='osx')


def read_file(filename, artist):
    file = open(file=filename, mode='r', encoding='utf-8')
    s = json.load(file)
    album_count = s['result']['albumCount']
    for i in range(album_count):
        album_name = s['result']['albums'][i]['name']
        dir_path = '{}/{}/'.format(artist, album_name)
        os.mkdir(dir_path)
        json_file = dir_path + '{}.json'.format(album_name)
        file = open(file=json_file, mode='w', encoding='utf-8')
        response = get_album_info(s['result']['albums'][i]['id'])
        json.dump(response.json(), file, ensure_ascii=False)
        file.close()
        handle_music(dir_path=dir_path, path=json_file)
        time.sleep(2)


def get_album_info(album_id):
    url = base_url + str(album_id)
    response = requests.get(url=url, headers=headers)
    return response


def handle_music(dir_path, path):
    json_path = path
    file = open(file=json_path, mode='r', encoding='utf-8')
    s = json.load(file)
    for item in s['album']['songs']:
        file_path = dir_path + item['name'] + '.mp3'
        # start download
        download_music(item['id'], file_path)
        time.sleep(1)


def download_music(song_id, file_path):
    song_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
    opener = request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    request.install_opener(opener)
    request.urlretrieve(song_url, file_path)


if __name__ == '__main__':
    artist = '李荣浩'
    file_name = '{}/{}.json'.format(artist, artist)
    read_file(filename=file_name, artist=artist)
