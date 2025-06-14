from transformers import pipeline
import torch
from enum import Enum
import time
import logging
import os


class WhisperLanguageID(str, Enum):

    english = 'english'
    chinese_mandarin = 'zh'
    malay = "zlm"

model_id = "openai/whisper-large-v3"

audio_path = "../../../../data/mandarin/audio/realstudy"
audio_file_name = 'naming_object_1.mp3'
audio_abs_path = os.path.join(audio_path, audio_file_name)

pipe = pipeline("automatic-speech-recognition", 
                model=model_id,
                generate_kwargs={"language": WhisperLanguageID.chinese_mandarin.value, "temperature": 0.0}, #, "beam_size": 5},
                return_timestamps=True)

if __name__ == "__main__":
    
    result = pipe(audio_abs_path)

    print(result["text"])
    