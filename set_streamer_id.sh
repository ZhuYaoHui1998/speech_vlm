#!/bin/bash
curl --location 'http://192.168.49.101:5010/api/v1/live-stream' \
--header 'Content-Type: application/json' \
--data '{"liveStreamUrl": "rtsp://admin:IHFXnM8k@192.168.49.15:554//Streaming/Channels/1"}'
# rtsp://admin:IHFXnM8k@192.168.49.15:554//Streaming/Channels/1
