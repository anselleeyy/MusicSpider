from pymongo import MongoClient


class Mongo:
    def __init__(self):
        self.host = '10.11.124.102'
        self.port = 27017
        self.client = MongoClient(host=self.host, port=self.port)
        self.db = self.client.music
        # my_set = db.li

    def save_album_info(self, data, artist):
        collections = self.db.album
        collections.update({"artist": artist}, {"$push": {"albums": data}})
        return

    def find_if_exist(self, artist, album):
        collections = self.db.album
        result = collections.find({"artist": artist, "albums.name": album})
        print(result)
        return result.count()
