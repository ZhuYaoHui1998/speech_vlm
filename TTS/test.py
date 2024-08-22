import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

api = TTS("tts_models/en/ljspeech/glow-tts").to(device)

api.tts_with_vc_to_file(
    "Hello everyone?",
    speaker_wav="./example_1.wav",
    file_path="output.wav"
)