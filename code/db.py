import pymysql, time
from code import Commons
from code.store import Store

class DB:
    def __init__(self):
        self.host = Commons.MYSQL['host']
        self.username = Commons.MYSQL['username']
        self.password = Commons.MYSQL['password']
        self.schema = Commons.MYSQL['schema']
        self.db = pymysql.connect(self.host, self.username, self.password, self.schema)
        self.store = Store()

    # 保存歌手相关信息
    def save_artist_info(self, artist_info):
        artist_id = artist_info['id']
        artist_name = self.format_param(artist_info['name'])
        pic_url = self.format_param(pymysql.escape_string(self.store.download(url=artist_info['picUrl'], path=str(artist_info['id']))))
        # SQL 插入语句
        sql = "INSERT INTO t_artist VALUES ({}, {}, {})".format(artist_id, artist_name, pic_url)
        cursor = self.db.cursor()
        # 新增该歌手的信息
        try:
            cursor.execute(sql)
            self.db.commit()
            print("save artist: {}'s info success".format(artist_name))
        except Exception as e:
            self.db.rollback()
            print(e)
        return artist_id

    # 保存单张专辑信息
    def save_album_info(self, artist_id, album_info, pic_url):
        album_id = album_info['id']
        album_name = self.format_param(album_info['name'])
        comment_thread_id = self.format_param(album_info['commentThreadId'])
        company = self.format_param(album_info['company'])
        description = self.format_param(album_info['description'])
        pic_url = self.format_param(pymysql.escape_string(pic_url))
        publishTime = self.format_timestamp(album_info['publishTime'])
        size = album_info['size']
        tags = self.format_param(album_info['tags'])
        # SQL 插入语句
        sql = "INSERT INTO t_album VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(album_id, album_name, artist_id, comment_thread_id, company, description, pic_url, publishTime, size, tags)
        cursor = self.db.cursor()
        # 新增一条专辑信息
        try:
            cursor.execute(sql)
            self.db.commit()
            print("\tsave album: {}'s info success".format(album_name))
        except Exception as e:
            self.db.rollback()
            print(e)
        return

    # 保存歌曲信息
    def save_music_info(self, song_info, album_id, mp3Url, lyric):
        song_id = song_info['id']
        lyric = self.format_param(lyric)
        mp3Url = self.format_param(pymysql.escape_string(mp3Url))
        song_name = self.format_param(song_info['name'])
        # SQL 插入语句
        sql = "INSERT INTO t_song VALUES ({}, {}, {}, {}, {})".format(song_id, album_id, lyric, mp3Url, song_name)
        cursor = self.db.cursor()
        # 新增一条专辑信息
        try:
            cursor.execute(sql)
            self.db.commit()
            print("\t\tsave song: {}'s info success".format(song_name))
        except Exception as e:
            self.db.rollback()
            print(e)
        return

    @staticmethod
    def format_param(param):
        if param == None:
            param = ""
        return "'" + param + "'"

    @staticmethod
    def format_timestamp(timestamp):
        timeStamp = timestamp / 1000
        dataTime = time.localtime(timeStamp)
        format_time = time.strftime("%Y-%m-%d %H:%M:%S", dataTime)
        return "'" + format_time + "'"
