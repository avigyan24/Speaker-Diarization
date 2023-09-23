
from pathlib import Path
from pyannote.audio import Pipeline


pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization",
                                    use_auth_token="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")

def predict_pipeline(wav):
    diarization = pipeline(wav)
    return diarization