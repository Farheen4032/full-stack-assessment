#!/bin/bash

url="https://www.amfiindia.com/spages/NAVAll.txt"
output="mutual_funds.tsv"

curl -s $url | awk -F ';' 'NR>1 && NF>4 {print $4 "\t" $5}' > $output

echo "Data saved to $output"
