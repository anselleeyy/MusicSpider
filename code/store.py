from code import Commons
import os, json


class Store:
    def __init__(self):
        self.root = Commons.dir_root

    def save_artist_info(self, artist, info):
        # 目录地址
        dir_path = self.root + '{}'.format(artist)
        # 文件夹不存在，则创建
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        path = dir_path + '{}.json'.format(artist)
        file = open(path, 'w', encoding='utf-8')
        json.dump(info, file, ensure_ascii=False)
        print('---------- artist: %s info saved ----------' % artist)
        file.close()
        return path

    def save_album_info(self, artist, info):
        # 目录地址
        dir_path = self.root + '{}'.format(artist)
        # 文件夹不存在，则创建
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        path = dir_path + '{}.json'.format(artist)
        file = open(path, 'w', encoding='utf-8')
        json.dump(info, file, ensure_ascii=False)
        print('---------- artist: %s albums info saved ----------' % artist)
        file.close()
        return path
