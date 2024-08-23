#!/bin/bash
curl --location 'http://192.168.49.227:5010/api/v1/chat/completions' \
--header 'Content-Type: application/json' \
--data '{
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."

        },
        {
            "role": "user",
            "content":[
                {
                    "type": "stream",
                    "stream":
                    {
                        "stream_id": "7d50edd6-a8f1-41b6-9eed-8ed874efd5a4"
                    }
                },

                {
                    "type":"text",
                    "text": "Can you scan it"
                }
            ]
        }
    ],
    "min_tokens": 1,
    "max_tokens": 128
}
'