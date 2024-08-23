#!/bin/bash
curl --location 'http://192.168.49.227:5010/api/v1/live-stream' \
--header 'Content-Type: application/json' \
--data '{"liveStreamUrl": "rtsp://192.168.49.227:31554/nvstream/root/store/nvstreamer_videos/sample_1080p_h264.mp4"}'
# rtsp://admin:IHFXnM8k@192.168.49.15:554//Streaming/Channels/1
# efe1cbe1-6d7f-4e76-b93c-ecec8660b543