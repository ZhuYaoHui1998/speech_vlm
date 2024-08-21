import pyaudio
import wave
import keyboard
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess
import time

# Configuration parameters
FORMAT = pyaudio.paInt16  # 16-bit resolution
CHANNELS = 1  # Mono channel
RATE = 16000  # 16kHz sample rate
CHUNK = 1024  # Number of samples per chunk
OUTPUT_FILENAME = "output.wav"  # Output file name

# Initialize PyAudio
audio = pyaudio.PyAudio()
# Prepare the list to store recording data
frames = []

# Initialize the model
model = "./SenseVoiceSmall"
model = AutoModel(
    model=model,
    vad_model="./speech_fsmn_vad_zh-cn-16k-common-pytorch",
    vad_kwargs={"max_single_segment_time": 30000},
    trust_remote_code=True,
    disable_log=True
)

def start_recording():
    global frames
    frames = []
    
    try:
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        print("Recording started... Press 'E' to stop recording.")
    
        while True:
            if keyboard.is_pressed('e'):
                print("Recording stopped.")
                break
            data = stream.read(CHUNK)
            frames.append(data)
    
        stream.stop_stream()
        stream.close()
    
    except Exception as e:
        print(f"An error occurred during recording: {e}")

def save_recording():
    try:
        waveFile = wave.open(OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        print(f"Recording saved as {OUTPUT_FILENAME}")
    except Exception as e:
        print(f"An error occurred while saving the recording: {e}")

print("Welcome to the Recording and Speech-to-Text System!")
print("Press 'S' to start recording, 'E' to stop recording.")

while True:
    if keyboard.is_pressed('s'):
        print("Preparing to start recording...")
        start_recording()
        save_recording()
        
        print("Processing the recording file, please wait...")
        try:
            res = model.generate(
                input=f"./{OUTPUT_FILENAME}",
                cache={},
                language="auto",  # "zh", "en", "yue", "ja", "ko", "nospeech"
                use_itn=True,
                batch_size_s=60,
                merge_vad=True,
                merge_length_s=15,
            )
            text = rich_transcription_postprocess(res[0]["text"])
            print(f"Speech-to-Text Result:\n{text}")
        except Exception as e:
            print(f"An error occurred while processing the recording: {e}")
        
    time.sleep(0.2)  # Reduce CPU usage
