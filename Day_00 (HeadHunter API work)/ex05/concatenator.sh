#!/bin/sh

echo '"id","created_at","name","has_test","alternate_url"' >> hh_positions.csv

for file in 2*.csv
do
    tail -n +2 ${file} >> hh_positions.csv
done