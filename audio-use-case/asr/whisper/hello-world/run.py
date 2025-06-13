from transformers import pipeline
import torch
from enum import Enum
import time
import logging
import os

class LanguageID(str, Enum):

    eng = 'english'
    cmn = 'chinese_mandarin'
    zlm = 'malay'

model_id = "openai/whisper-large-v3"

audio_path = "../../../../data/audio"
audio_file_name = 'eng.mp3'
audio_abs_path = os.path.join(audio_path, audio_file_name)
pipe = pipeline("automatic-speech-recognition", 
                model=model_id,
                model_kwargs={"language": "english"},
                generate_kwargs={"temperature": 0.0, "beam_size": 5},
                return_timestamps=True
                )

if __name__ == "__main__":
    
    result = pipe(audio_abs_path)

    print(result["text"])
    