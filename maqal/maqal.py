# encoding=utf-8
# Maqal

import os
import json
import sqlite3


class Maqal():

    dbObject = None
    mainList = []
    modulePath = os.path.dirname(__file__)
    jsonFile = modulePath + "/storage/uyghur-maqal-temsilliri.json"
    dbFile = modulePath + "/storage/uyghur-maqal-temsilliri.db"

    def __init__(self):
        exist = os.path.isfile(self.dbFile)
        self.dbObject  = sqlite3.connect(self.dbFile, check_same_thread=False)
        if not exist:
            self.readFile()
            self.makeDb()
        # self.dbObject.close()

    def readFile(self):
        if not os.path.isfile(self.jsonFile):
            return
        with open(self.jsonFile, "r", encoding="utf-8") as f:
            mainText = f.read()
            self.mainList = json.loads(mainText)
        pass

    def makeDb(self):
        cursor = self.dbObject.cursor()
        cursor.execute("DROP TABLE IF EXISTS maqal")
        cursor.execute('''
            CREATE TABLE maqal (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                txt TEXT
            );
        ''')
        for text in self.mainList:
            cursor.execute("INSERT INTO 'maqal' (txt) VALUES ('" + text + "');")
        self.dbObject.commit()

    def random(self):
        cursor = self.dbObject.cursor()
        lines = cursor.execute("SELECT * FROM maqal ORDER BY RANDOM() LIMIT 1;")
        for line in lines:
            return line[1]

    def search(self, query):
        cursor = self.dbObject.cursor()
        lines = cursor.execute("SELECT * FROM maqal WHERE txt LIKE '%" + query + "%'")
        texts = []
        for line in lines:
            texts.insert(1, line[1])
        return texts


if __name__ == "__main__":
    maqal = Maqal()
    allLines = maqal.search("%")
    randomLine = maqal.random()
    print("Uyghur Maqal Temsilliri:", len(allLines))
    print(randomLine)
