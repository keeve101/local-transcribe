import subprocess
import os
from config import whisper_main, whisper_model
from pathlib import Path

ffmpeg_cmd = ["ffmpeg", "-i"]
transcribe_cmd = [
    whisper_main,
    "--no-timestamps",
    "true",
    "--model",
    whisper_model,
    "-f",
]

video_path = input("Provide the path to the video: ")

file_name = Path(video_path).stem

if video_path.endswith(".mp4"):
    subprocess.run(ffmpeg_cmd + [video_path, "-ar", "16000", file_name + ".wav"])

subprocess.run(transcribe_cmd + [file_name + ".wav", "--output-txt", "-of", file_name])

os.remove(file_name + ".wav")
