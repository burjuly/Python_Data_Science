#!/bin/sh

tail -n+2 ../ex03/hh_positions.csv | awk -F, '{file_name = substr($2, 2, 10); print > (file_name)}'

for file in *[^.csv][^.sh]
do
    (echo '"id","created_at","name","has_test","alternate_url"' | cat - ${file}) > "${file}.csv"
    rm ${file}
done


