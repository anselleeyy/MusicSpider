from pymongo import MongoClient
from code import Commons

class Mongo:
    def __init__(self):
        self.host = Commons.MONGO['host']
        self.port = Commons.MONGO['port']
        self.client = MongoClient(host=self.host, port=self.port)
        self.db = self.client.music
        self.collections = self.db.Artist
    
    # 保存歌手相关信息（Artist 集合）
    def save_artist_info(self, artist_info):
        # 处理歌手数据
        data = {
            "name": artist_info['name'],
            "_id": artist_info['id'],
            "picUrl": artist_info['picUrl']
        }
        self.collections = self.db.Artist
        # 开始保存
        result_id = self.collections.insert(data)
        return result_id

    # 根据歌手 id 查找 Album 中是否存在该条记录
    def check_artist_in_album(self, artist_id):
        self.collections = self.db.Album
        result = self.collections.find_one({"artist_id": artist_id})
        if result == None:
            self.collections.insert_one({"artist_id": artist_id})
            print("insert into artist: {} info".format(artist_id))
        return
    
    # 保存单张专辑信息（根据歌手 id 存储）
    def save_album_info(self, album_info, artist_id, pic_url):
        self.check_artist_in_album(artist_id=artist_id)
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
        self.collections = self.db.Album
        self.collections.update({"artist_id": artist_id}, {"$push": {"albums": data}})

    # 根据专辑 id 查找 Song 中是否存在该条记录
    def check_album_in_song(self, album_id):
        self.collections = self.db.Song
        result = self.collections.find_one({"album_id": album_id})
        if result == None:
            self.collections.insert_one({"album_id": album_id})
            print("insert into album: {} info".format(album_id))
        return
    
    # 保存歌曲信息
    def save_song_info(self, song_info, album_id, mp3Url, lyric):
        self.check_album_in_song(album_id=album_id)
        data = {
            "name": song_info['name'],
            "_id": song_info['id'],
            "mp3Url": mp3Url,
            "lyric": lyric
        }
        self.collections = self.db.Song
        self.collections.update({"album_id": album_id}, {"$push": {"songs": data}})
        return
