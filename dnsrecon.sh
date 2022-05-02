#!/bin/bash
for subdomain in $(cat subdomains.txt)
do
host $subdomain.$1 | grep -v "not found"
done
