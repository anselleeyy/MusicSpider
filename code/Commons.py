headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'music.163.com',
    'Referer': 'https://music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/70.0.3538.110 Safari/537.36'
}

dir_root = 'C:/Users/Ansel/Desktop/MusicSpider/music/'

search_url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token'

album_url = 'http://music.163.com/api/album/{}'

song_url = 'http://music.163.com/weapi/song/enhance/player/url?csrf_token='

lyric_url = 'https://music.163.com/weapi/song/lyric?csrf_token='
