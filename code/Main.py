import json
import os
from code.NetEase import Api
from code import Commons
from code.store import Store
from code.mongo import Mongo


def read_file(path):
    file = open(file=path, mode='r', encoding='utf-8')
    s = json.load(file)
    return s
    # album_count = s['result']['albumCount']
    # for i in range(album_count):
    #     album_name = s['result']['albums'][i]['name']
    #     dir_path = Commons.dir_root + '{}/{}/'.format(artist, album_name)
    #     # 文件夹不存在，则创建/
    #     if not os.path.exists(dir_path):
    #         os.mkdir(dir_path)
    #     json_file = dir_path + '{}.json'.format(album_name)
    #     file = open(file=json_file, mode='w', encoding='utf-8')
    #     api = Api()
    #     response = api.get_album_info(album_id=s['result']['albums'][i]['id'])
    #     json.dump(response.json(), file, ensure_ascii=False)
    #     file.close()


if __name__ == '__main__':
    param = ['李荣浩']
    api = Api()
    store = Store()
    # 遍历歌手参数
    for artist in param:
        # 得到当前歌手信息并保存
        artist_info = api.get_artist_info(artist=artist)
        artist_info_path = store.save_artist_info(artist=artist, info=artist_info)
        # 获取专辑信息
        album_info = api.get_artist_album_list(artist=artist)
        album_info_path = store.save_album_info(artist=artist, info=album_info)
        # 遍历专辑信息
        albums = read_file(path=album_info_path)
        count = 0
        for i in range(30):
            item = albums['result']['albums'][i]
            data = {
                "name": item['name'],
                "id": item['id'],
                "size": item['size'],
                "picUrl": item['picUrl'],
                "publishTime": item['publishTime'],
                "commentThreadId": item['commentThreadId'],
                "description": item['description'],
                "tags": item['tags'],
                "company": item['company']
            }
            mongo = Mongo()
            if mongo.find_if_exist(artist=artist, album=item['name']) == 0:
                mongo.save_album_info(data=data, artist=artist)
                count += 1
            # 获取当前专辑内音乐信息

        print('---------- {} albums saved ----------'.format(count))
        # 持久化存储



    # api.get_artist_album_list(artist=param)
    # file_name = Commons.dir_root + '{}/{}.json'.format(param, param)
    # read_file(filename=file_name, artist=param)
    # id = 1318235595
    # print(api.get_song_lyric(id))
