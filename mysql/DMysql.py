import MySQLdb
class DMysql:
    def __init__(self):
        self.db = MySQLdb.connect('127.0.0.1','root','root','test')
        self.cursor = self.db.cursor()
    def findOne(self,sql):
        self.cursor.execute(sql)
        info = self.cursor.fetchone()
        return info
    def findArr(self,sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        data = []
        for row in results:
            data.append(row)
        return data
