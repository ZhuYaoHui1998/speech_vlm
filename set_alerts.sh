#!/bin/bash

curl --location 'http://192.168.49.227:5010/api/v1/alerts' \
--header 'Content-Type: application/json' \
--data '{
    "alerts": ["is there a chair?"],
    "id": "1388b691-3b9f-4bda-9d70-0ff0696f80f4"
}'
#7d50edd6-a8f1-41b6-9eed-8ed874efd5a4