from code import Commons
import os, json


class Store:
    def __init__(self):
        self.root = Commons.DIR_ROOT

    # 保存歌手所有专辑信息到本地（Json 文件）
    def save_all_album_info(self, artist, info):
        # 目录地址
        dir_path = self.root + '{}/'.format(artist)
        # 文件夹不存在，则创建
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        path = dir_path + '{}.json'.format(artist)
        file = open(path, 'w', encoding='utf-8')
        json.dump(info, file, ensure_ascii=False, indent=4)
        print('---------- artist: %s albums info saved ----------' % artist)
        file.close()
        return path

    # 保存单个专辑信息到本地（Json 文件）
    def save_album_info(self, artist, album_name, info):
        # 目录地址
        dir_path = self.root + '{}/{}/'.format(artist, album_name)
        # 文件夹不存在，则创建
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        path = dir_path + '{}.json'.format(album_name)
        file = open(path, 'w', encoding='utf-8')
        json.dump(info, file, ensure_ascii=False, indent=4)
        print('---------- artist: %s \'s album: %s info saved ----------' % (artist, album_name))
        file.close()
        return path
