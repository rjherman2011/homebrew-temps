import os
import sqlite3

TEMPLOG_DIR = "/home/pi/homebrewTemps/temperatureLogs"

data = []

for filename in os.listdir(TEMPLOG_DIR):
    with open(TEMPLOG_DIR + "/" + filename) as file:
        for line in file:
            if line.startswith('#'):
                continue
            fileLine = line.replace("\n", "")
            data.append(tuple(fileLine.split(',')))

db = sqlite3.connect('../data/beerLogsDb')

cursor = db.cursor()

cursor.executemany('''
INSERT INTO temperatures(timestamp, inTemp, outTemp) VALUES(?, ?, ?)
''', data)

db.commit()
