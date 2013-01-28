#!/usr/bin/env python
# -*- coding: UTF-8; -*-

'''
Import all_locations.txt into locations.db
'''

import string, sys
import sqlite3 as lite

conn = lite.connect('locations.db')
conn.text_factory = str
cursor = conn.cursor()

cursor.execute("DELETE FROM locations")

query = "INSERT INTO locations (name, country, xml) VALUES (?, ?, ?);"
fd = open( "all_locations.txt" )
content = fd.readline()
while (content != "" ):
  fields = string.split(content, ',')
  cursor.execute(query, (fields[0], fields[1].strip(), fields[2].strip()))
  content = fd.readline()  
conn.commit()
conn.close()

