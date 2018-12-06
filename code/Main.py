import json
import os
from code.NetEase import Api
from code import Commons


def read_file(filename, artist):
    file = open(file=filename, mode='r', encoding='utf-8')
    s = json.load(file)
    album_count = s['result']['albumCount']
    for i in range(album_count):
        album_name = s['result']['albums'][i]['name']
        dir_path = Commons.dir_root + '{}/{}/'.format(artist, album_name)
        # 文件夹不存在，则创建
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        json_file = dir_path + '{}.json'.format(album_name)
        file = open(file=json_file, mode='w', encoding='utf-8')
        api = Api()
        response = api.get_album_info(album_id=s['result']['albums'][i]['id'])
        json.dump(response.json(), file, ensure_ascii=False)
        file.close()


if __name__ == '__main__':
    param = '李荣浩'
    api = Api()
    # api.get_artist_album_list(artist=param)
    # file_name = Commons.dir_root + '{}/{}.json'.format(param, param)
    # read_file(filename=file_name, artist=param)
    id = 1318235595
    print(api.get_song_lyric(id))
