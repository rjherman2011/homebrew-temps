import sqlite3

#create or open a file called beerLogsDb
db = sqlite3.connect('../data/beerLogsDb')

#get a cursor object
cursor = db.cursor()
#create beer table
#Id(pk)
#Description (varchar)
cursor.execute('''
CREATE TABLE beer(
beerId INTEGER PRIMARY KEY,
description TEXT
);
''')
print('Beer table created')
#create beer detail table (still in progress)
#Id(pk)
#fkBeerId (fk beerTable.Id)
#Date Brewed (timestamp)
#Date Bottled (timetstamp)
#Date "Done" (timestamp)
#OG (decimal)
#FG (decimal)
#Rating (int (1-5 star))
#AdditionalDetails (varchar (JSON text for flexibility))
cursor.execute('''
CREATE TABLE beerDetail(
beerDetailId INTEGER PRIMARY KEY,
beerId INTEGER,
dateBrewed TIMESTAMP,
dateBottled TIMESTAMP,
dateDone TIMESTAMP,
OG REAL,
FG REAL,
rating INTEGER,
additionalDetails TEXT,
FOREIGN KEY(beerId) REFERENCES beer(beerId)
)
''')
print('Beer Detail table created')
#create temperature table
#Id(pk)
#fkBeerId (Optional fk beerTable.Id)
#timestamp
#InTemp (decimal)
#OutTemp (decimal)
cursor.execute('''
CREATE TABLE temperatures(
id INTEGER PRIMARY KEY,
beerId INTEGER NULL,
timestamp TIMESTAMP,
inTemp REAL,
outTemp REAL,

FOREIGN KEY(beerId) REFERENCES beer(beerId)
)
''')
print('Temperature table created')

db.commit() #commit everything
