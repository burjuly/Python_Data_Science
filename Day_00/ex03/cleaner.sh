#!/bin/sh

head -n 1 ../ex02/hh_sorted.csv > hh_positions.csv
tail -n+2 ../ex02/hh_sorted.csv | 
awk -F "\",\"|\",|,\"" -v OFS="," \
'{ if (index(toupper($3), "JUNIOR") != 0) {$3 = "\"Junior\""}
else if (index(toupper($3), "MIDDLE") != 0) {$3 = "\"Middle\""}
else if (index(toupper($3), "SENIOR") != 0) {$3 = "\"Senior\""}
else if (index(toupper($3), "JUNIOR/MIDDLE") != 0) {$3 = "\"Junior/Middle\""}
else if (index(toupper($3), "MIDDLE/SENIOR") != 0) {$3 = "\"Middle/Senior\""} 
else {$3 = "\"-\""}; {$1 = $1 "\""}; {$2 = "\"" $2 "\""}; {$5 = "\"" $5 }; print $0 }' >> hh_positions.csv
