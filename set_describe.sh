#!/bin/bash
curl --location 'http://192.168.49.101:5010/api/v1/chat/completions' \
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
                        "stream_id": "d027088e-9ba9-40b9-8481-c306e35df8b6"
                    }
                },

                {
                    "type":"text",
                    "text": "describe the scene"
                }
            ]
        }
    ],
    "min_tokens": 1,
    "max_tokens": 128
}
'