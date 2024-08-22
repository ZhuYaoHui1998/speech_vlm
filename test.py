import torch
from TTS.api import TTS

import pyaudio
import wave
import subprocess

p = pyaudio.PyAudio()

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Init TTS
api = TTS("tts_models/en/ljspeech/glow-tts").to(device)



api.tts_to_file(
    "You can also try TTS without install with the docker image. Simply run the following command and you will be able to run TTS without installing it.",
    speaker_wav="./example_1.wav",
    file_path="speech.wav"
)
subprocess.run(['ffmpeg', '-i', 'speech.wav', '-ar', '48000', 'speech1.wav','-y'])

wf = wave.open('./speech1.wav', 'rb')
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=48000,
                output=True,
                output_device_index=24)
data = wf.readframes(1024)
while data:
    stream.write(data)
    data = wf.readframes(1024)
stream.stop_stream()
stream.close()
p.terminate()