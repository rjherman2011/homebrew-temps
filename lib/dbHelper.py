import sqlite3
from datetime import datetime, timedelta

DB_FILE = "/home/pi/homebrewTemps/data/beerLogsDb"
ISO_FORMAT = "%Y-%m-%dT%H:%M:%S"

#get temp data as lines method
def get_temps(numHours):
    lines = []

    db = get_db()
    cursor = get_cursor(db)
    nowDate = datetime.now()
    firstDate = nowDate - timedelta(hours=numHours)

    cursor.execute('''
    SELECT timestamp, inTemp, outTemp
    FROM temperatures
    WHERE timestamp BETWEEN ? AND ?
    ''', (format_date(firstDate), format_date(nowDate)))

    all_rows = cursor.fetchall()

    for row in all_rows:
        lines.append('{0},{1},{2}'.format(row[0], row[1], row[2]))
    
    return lines

def log_temps(tempTuple):
    db = get_db()
    cursor = get_cursor(db)

    cursor.execute('''
    INSERT INTO temperatures(timestamp, inTemp, outTemp) VALUES(?, ?, ?)
    ''', (datetime.now().strftime(ISO_FORMAT), tempTuple[0], tempTuple[1]))

    db.commit()
    db.close()

def get_db():
    db = sqlite3.connect(DB_FILE)
    db.row_factory = sqlite3.Row
    return db

def get_cursor(db):
    cursor = db.cursor()
    return cursor

def format_date(dateTime):
    return dateTime.strftime(ISO_FORMAT)
