#!/usr/bin/env python
# -*- coding: UTF-8; -*-

'''
Import files (countries.txt, all_places.txt) into places.db
'''

import string, sys
import sqlite3 as lite

def get_db_cursor ():
  conn = lite.connect('places.db')
  conn.text_factory = str
  return conn, conn.cursor()


def clear_db (cursor, table):
  query = "delete from " + table
  cursor.execute(query)


def insert_row_countries (cursor, fields):
  query = "INSERT INTO countries (countrycode, countryname) VALUES (?, ?);"
  
  country_code = all_lower(fields[0])
  country_name = all_lower(fields[1])

  return cursor.execute(query, (country_code, country_name))


def insert_row_world (cursor, fields, country_mapping):
  query = "INSERT INTO places (countryid, placename, xml) VALUES (?, ?, ?);"
  
  countryid = country_mapping[all_lower(fields[0])]
  placename = fields[1].strip()
  # countryname in fields[2] is not in use here, already mapped to the country table
  xml = fields[3].strip()
  
  return cursor.execute(query, (countryid, placename, xml))

def create_country_mapping (cursor):
	cursor.execute("SELECT countryid,countrycode FROM countries;")
	rows = cursor.fetchall()
	mapping = {}
	for row in rows:
		mapping[row[1]] = row[0]
	
	return mapping
	

def process_file_countries (cursor):
  fd = open( "countries.txt" )
  content = fd.readline()
  while (content != "" ):
    fields = string.split(content, ',')
    insert_row_countries(cursor, fields)
    content = fd.readline()


def process_file_all_places (cursor, country_mapping):
  fd = open( "all_places.txt" )
  content = fd.readline() #header
  content = fd.readline()
  while (content != "" ):
    fields = string.split(content, ',')
    result = insert_row_world(cursor, fields, country_mapping)
    content = fd.readline()


def all_lower (str):
  return str.strip().lower().replace('Æ', 'æ').replace('Ø', 'ø').replace('Å', 'å')

try: 

	conn, c = get_db_cursor ()
	clear_db (c, 'countries')
	clear_db (c, 'places')
	process_file_countries (c)
	country_mapping = create_country_mapping(c)
	process_file_all_places(c, country_mapping)
	
	conn.commit()
	conn.close()
	
except lite.Error, e:
        
    print "Error %s:" % e.args[0]

