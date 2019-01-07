from code.pmongo import Pmongo

mongo = Pmongo()
artist_info = {
    "name": "李荣浩",
    "id": 3419,
    "picUrl": "https://blog.csdn.net/u013205877/article/details/76037540"
}

album_info = {
    "name": "",
    "id": 35457526,
    "size": 1,
    "picUrl": "",
    "publishTime": 1494007977282,
    "commentThreadId": "",
    "description": "",
    "tags": "",
    "company": ""
}

if __name__ == "__main__":
    mongo.save_album_info(album_info=album_info, artist_id=3417, pic_url="https://blog.csdn.net/u013205877/article/details/76037540")