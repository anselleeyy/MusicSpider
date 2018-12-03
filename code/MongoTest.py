from pymongo import MongoClient
import json

host = '10.11.124.102'
port = 27017
client = MongoClient(host=host, port=port)
db = client.music
my_set = db.li

data = [
    {
        "name": "耳朵",
        "id": 73914415,
        "picUrl": "https://p1.music.126.net/tt8xwK-ASC2iqXNUXYKoDQ==/109951163606377163.jpg",
        "size": 10,
        "publishTime": 1539705600007,
        "company": "华纳音乐",
        "commentThreadId": "R_AL_3_73914415"
    },
    {
        "name": "戒烟",
        "id": "36796018",
        "picUrl": "https://p1.music.126.net/rVkRzdKkIqVxRjDhN4LFHQ==/18342052975051883.jpg",
        "size": 1,
        "publishTime": 1510588800007,
        "company": "华纳唱片",
        "commentThreadId": "R_AL_3_36796018"
    }
]


def save_info_to_mongo(artist):
    file_name = '{}/{}.json'.format(artist, artist)
    file = open(file=file_name, mode='r', encoding='utf-8')
    s = json.load(file)
    count = 0
    for i in s['result']['albums']:
        data = {
            "name": "耳朵",
            "id": 73914415,
            "picUrl": "https://p1.music.126.net/tt8xwK-ASC2iqXNUXYKoDQ==/109951163606377163.jpg",
            "size": 10,
            "publishTime": 1539705600007,
            "company": "华纳音乐",
            "commentThreadId": "R_AL_3_73914415"
        }
    my_set.insert(data)
    print(count)


if __name__ == '__main__':
    param = '李荣浩'
    save_info_to_mongo(artist=param)