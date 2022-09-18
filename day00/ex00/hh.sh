#!/bin/sh
if [ $# -eq 1 ]; then
	vacancy=$( echo $1 | tr ' ' '-')
	curl -k "https://api.hh.ru/vacancies?text=${vacancy}&per_page=20" | jq > hh.json
else
	echo "Vacancy name must contain at least 1 sign"
fi
