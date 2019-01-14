import pymysql
from code import Commons

class DB:
    def __init__(self):
        self.host = Commons.MYSQL['host']
        self.username = Commons.MYSQL['username']
        self.password = Commons.MYSQL['password']
        self.schema = Commons.MYSQL['schema']
        self.db = pymysql.connect(self.host, self.username, self.password, self.schema)
    
    def tet(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print ("Database version : %s " % data)
        self.db.close()


if __name__ == "__main__":
    db = DB()
    db.tet()