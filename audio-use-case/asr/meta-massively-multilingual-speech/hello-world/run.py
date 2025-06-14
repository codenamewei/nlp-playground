from transformers import pipeline
import torch
from enum import Enum
import time
import logging
import os

class MMSLanguageID(str, Enum):

    english = 'eng'
    chinese_mandarin = 'cmn'
    malay = "zlm"

model_id = "facebook/mms-1b-all"

audio_path = "../../../../data/audio"
audio_file_name = 'eng.mp3'
audio_abs_path = os.path.join(audio_path, audio_file_name)
pipe = pipeline(model=model_id, model_kwargs={"target_lang": MMSLanguageID.english.value, "ignore_mismatched_sizes": True})


if __name__ == "__main__":
    
    result = pipe(audio_abs_path)

    print(result["text"])
    