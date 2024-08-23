#!/bin/bash

curl --location 'http://192.168.49.227:5010/api/v1/alerts' \
--header 'Content-Type: application/json' \
--data '{
    "alerts": ["is there a chair?"],
    "id": "f4c16653-8038-43f2-a759-8e8d44039510"
}'
#7d50edd6-a8f1-41b6-9eed-8ed874efd5a4
