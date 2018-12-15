import os
from code.NetEase import Api
from code import Commons
from code.store import Store
from code.mongo import Mongo


if __name__ == '__main__':
    param = Commons.artists
    api = Api()
    store = Store()
    mongo = Mongo()
    # 遍历歌手参数
    for artist in param:
        # 得到当前歌手信息并保存
        artist_info = api.get_artist_info(artist=artist)
        _id = mongo.save_artist_info(artist_info=artist_info['result']['artists'][0])
        print(_id)
        # 获取歌手所有专辑信息并保存
        album_info = api.get_artist_album_list(artist=artist)
        album_info_path = store.save_all_album_info(_id=_id, artist=artist, info=album_info)
        # 遍历专辑信息
        albums = store.read_file(path=album_info_path)
        # 实际专辑数量
        count = 0
        album_count = albums['result']['albumCount']
        # 每个歌手的专辑数量不得超过MAX_SIZE（这里我们选择30）
        # 同时判断当前歌手的专辑数量是否超过30
        album_count = album_count if (album_count < Commons.ALBUM_MAX_SIZE) else Commons.ALBUM_MAX_SIZE
        for i in range(2):
            item = albums['result']['albums'][i]
            # 避免同名专辑存在（尚没有解决同歌手的同名专辑问题）
            if mongo.find_if_exist(artist=artist, album=item['name']) != 0:
                continue
            # 下载专辑图片
            picUrl = store.download(url=item['picUrl'], path=os.path.join(str(_id), str(item['id'])))
            mongo.save_album_info(album_info=item, artist=artist, pic_url=picUrl)
            count += 1
            # 获取当前专辑内音乐信息
            music_info = api.get_album_info(album_id=item['id'])
            music_info_path = store.save_album_info(_id=_id, album_id=item['id'], artist=artist, album_name=item['name'], info=music_info)
            # 遍历专辑内音乐信息
            musics = store.read_file(path=music_info_path)
            for song in musics['album']['songs']:
                song_id = song['id']
                mp3Url = api.get_music_url(ids=song_id)
                path = store.download(url=mp3Url, path=os.path.join(str(_id), str(item['id'])))
                lyric = api.get_song_lyric(ids=song_id)
                mongo.save_music_info(song_info=song, album_name=item['name'], artist=artist, mp3Url=path, lyric=lyric)
        # 更新歌手专辑数量
        mongo.update_album_count(artist=artist, album_count=count)
        print('---------- {} albums saved ----------'.format(count))
