import json
import os
from urllib import request

from code import Commons


class Store:
    def __init__(self):
        self.root = Commons.DOWNLOAD_DIR
        self.opener = request.build_opener()
        self.opener.addheaders = [('User-Agent', 'Mozilla/5.0')]

    # 保存歌手所有专辑信息到本地（Json 文件）
    def save_all_album_info(self, _id, artist, info):
        # 目录地址
        dir_path = self.root + '{}/'.format(_id)
        # 文件夹不存在，则创建
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        file_path = dir_path + '{}.json'.format(artist)
        file = open(file_path, 'w', encoding='utf-8')
        json.dump(info, file, ensure_ascii=False, indent=4)
        print('---------- artist: %s albums info saved ----------' % artist)
        file.close()
        return file_path

    # 保存单个专辑信息到本地（Json 文件）
    def save_album_info(self, _id, album_id, artist, album_name, info):
        # 目录地址
        dir_path = self.root + '{}/{}/'.format(_id, album_id)
        # 文件夹不存在，则创建
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        file_path = dir_path + '{}.json'.format(album_name)
        file = open(file_path, 'w', encoding='utf-8')
        json.dump(info, file, ensure_ascii=False, indent=4)
        print('---------- artist: %s \'s album: %s info saved ----------' % (artist, album_name))
        file.close()
        return file_path

    # 下载工具（包括音乐、图片）
    def download(self, url, path):
        dir_path = self.root + path
        request.install_opener(self.opener)
        file_name = url.split('/').pop()
        # 判断目录是否存在，如果不存在，则创建
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_path = os.path.join(dir_path, file_name)
        print(file_path)
        request.urlretrieve(url=url, filename=file_path)
        return file_path

    # 读取本地保存的 json 文件
    @staticmethod
    def read_file(path):
        file = open(file=path, mode='r', encoding='utf-8')
        s = json.load(file)
        return s
