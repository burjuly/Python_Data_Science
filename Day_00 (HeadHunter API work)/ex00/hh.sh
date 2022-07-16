#!/bin/sh

curl -G -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'  \
--data-urlencode "text=${1}" \
--data-urlencode  'per_page=20' \
--data-urlencode  'page=0' \
https://api.hh.ru/vacancies | jq '.' > hh.json
