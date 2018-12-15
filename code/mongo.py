from pymongo import MongoClient


class Mongo:
    def __init__(self):
        self.host = '10.11.124.102'
        self.port = 27017
        self.client = MongoClient(host=self.host, port=self.port)
        self.db = self.client.music
        self.collections = self.db.album

    # 保存歌手相关信息
    def save_artist_info(self, artist_info):
        # 处理歌手信息
        data = {
            "name": artist_info['name'],
            "_id": artist_info['id'],
            "picUrl": artist_info['picUrl']
        }
        # 新增该歌手的信息
        result_id = self.collections.insert({"artist": data})
        return result_id

    # 保存单张专辑信息
    def save_album_info(self, album_info, artist, pic_url):
        data = {
            "name": album_info['name'],
            "_id": album_info['id'],
            "size": album_info['size'],
            "picUrl": pic_url,
            "publishTime": album_info['publishTime'],
            "commentThreadId": album_info['commentThreadId'],
            "description": album_info['description'],
            "tags": album_info['tags'],
            "company": album_info['company']
        }
        self.collections.update({"artist.name": artist}, {"$push": {"albums": data}})
        return

    # 判断专辑是否存在
    def find_if_exist(self, artist, album):
        result = self.collections.find({"artist.name": artist, "albums.name": album})
        return result.count()

    # 保存歌曲信息
    def save_music_info(self, song_info, album_name, artist, mp3Url, lyric):
        data = {
            "name": song_info['name'],
            "_id": song_info['id'],
            "mp3Url": mp3Url,
            "lyric": lyric
        }
        self.collections.update({"artist.name": artist, "albums.name": album_name}, {"$push": {"albums.$.songs": data}})
        return
