#!/bin/bash

# This file is used to parse location data with yr.no-URLs.
# Output is pushed into all_locations.txt. 
# Import file with 02-import-data.py

echo "Parsing norwegian locations - hourly forecast available"
tail -n+2 noreg.txt |cut -f 2,14 --output-delimiter=';' |awk 'BEGIN {FS =";"} {print $1 ",Norway,"$2 }' |sed 's/\/forecast.xml/\/forecast_hour_by_hour.xml/g' > all_locations.txt

echo "Parsing international locations - forecast every 6 hours (not by choice)"
cut -f4,11,18 --output-delimiter=, verda.txt >> all_locations.txt
