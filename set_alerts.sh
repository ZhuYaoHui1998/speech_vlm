#!/bin/bash

curl --location 'http://192.168.49.101:5010/api/v1/alerts' \
--header 'Content-Type: application/json' \
--data '{
    "alerts": ["is there person?"],
    "id": "d027088e-9ba9-40b9-8481-c306e35df8b6"
}'
