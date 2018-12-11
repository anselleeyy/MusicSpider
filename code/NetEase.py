from Crypto.Cipher import AES
import base64
import random
import codecs
import math
import json
import requests
from code import Commons


class Encrypt(object):
    def __init__(self, d):
        self.d = d
        self.e = '010001'
        self.f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5a' \
                 'a76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46be' \
                 'e255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.g = '0CoJUm6Qyw8W8jud'
        self.random_text = self.get_random_str()

    @staticmethod
    def get_random_str():
        """
        js中的a函数
        """
        alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        res = ''
        for x in range(16):
            index = math.floor(random.random() * len(alpha))
            res += alpha[index]
        return res

    @staticmethod
    def aes_encrypt(text, key):
        iv = '0102030405060708'
        pad = 16 - len(text.encode()) % 16
        text = text + pad * chr(pad)
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        msg = base64.b64encode(encryptor.encrypt(text))
        return msg

    @staticmethod
    def rsa_encrypt(value, text, modulus):
        """
        进行rsa加密
        """
        text = text[::-1]
        rs = int(codecs.encode(text.encode('utf-8'), 'hex-codec'), 16) ** int(value, 16) % int(modulus, 16)
        return format(rs, 'x').zfill(256)

    def get_data(self):
        params = self.aes_encrypt(self.d, self.g)
        params = self.aes_encrypt(params.decode('utf-8'), self.random_text)
        enc_sec_key = self.rsa_encrypt(self.e, self.random_text, self.f)
        return {
            'params': str(params, encoding='utf-8'),
            'encSecKey': enc_sec_key
        }


class Api:
    # 获取歌手信息，返回 json 数据
    @staticmethod
    def get_artist_info(artist):
        post_data = {
            "total": "True",
            "s": artist,
            "offset": 0,
            "csrf_token": "nothing",
            "limit": 1,
            "type": 100
        }
        encrypt_data = Encrypt(json.dumps(post_data)).get_data()
        response = requests.post(url=Commons.SEARCH_URL, data=encrypt_data, headers=Commons.headers)
        return response.json()

    # 获取歌手专辑列表（前30个），返回 json 数据
    @staticmethod
    def get_artist_album_list(artist):
        post_data = {
            "total": "True",
            "s": artist,
            "offset": 0,
            "csrf_token": "nothing",
            "limit": 30,
            "type": 10
        }
        encrypt_data = Encrypt(json.dumps(post_data)).get_data()
        response = requests.post(url=Commons.SEARCH_URL, data=encrypt_data, headers=Commons.headers)
        return response.json()

    # 获取专辑内音乐信息
    @staticmethod
    def get_album_info(album_id):
        url = Commons.ALBUM_URL.format(album_id)
        response = requests.get(url=url, headers=Commons.headers)
        return response.json()

    # 获取音乐播放地址，便于下载
    @staticmethod
    def get_music_url(ids, br=128000):
        text = {'ids': [ids], 'br': br, 'csrf_token': ''}
        wyy = Encrypt(json.dumps(text))
        data = wyy.get_data()
        response = requests.post(url=Commons.SONG_URL, data=data, headers=Commons.headers)
        return response.json()['data'][0]['url']

    # 获取音乐歌词信息
    @staticmethod
    def get_song_lyric(ids):
        text = {'id': ids, 'lv': -1, 'tv': -1, 'csrf_token': ''}
        wyy = Encrypt(json.dumps(text))
        data = wyy.get_data()
        response = requests.post(url=Commons.LYRIC_URL, data=data, headers=Commons.headers)
        return response.json()['lrc']['lyric']
