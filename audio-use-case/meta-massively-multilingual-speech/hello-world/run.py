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

model_id = "facebook/mms-1b-all"

audio_folder = "../../data/audio"
audio_path = ""
audio_abs_path = os.path.join(audio_folder, audio_path)
pipe = pipeline(model=model_id, model_kwargs={"target_lang": LanguageID.cmn.name, "ignore_mismatched_sizes": True})


if __name__ == "__main__":
    
    result = pipe(audio_path)

    print(result["text"])
    