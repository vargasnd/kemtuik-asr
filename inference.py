import torch
import librosa

from transformers import (
    WhisperProcessor,
    WhisperForConditionalGeneration
)


MODEL_DIR = "./model"


print("Loading model...")

processor = WhisperProcessor.from_pretrained(
    MODEL_DIR
)

model = WhisperForConditionalGeneration.from_pretrained(
    MODEL_DIR
)

# Jangan paksa bahasa Indonesia.
# Kemtuik bukan bahasa Indonesia.
model.config.forced_decoder_ids = None
model.config.suppress_tokens = []

device = "cuda" if torch.cuda.is_available() else "cpu"

model = model.to(device)
model.eval()

print(f"Model loaded on: {device}")


def transcribe_audio(audio_path):

    # Load audio menjadi mono 16 kHz
    audio, sr = librosa.load(
        audio_path,
        sr=16000,
        mono=True
    )

    # Extract Whisper features
    input_features = processor.feature_extractor(
        audio,
        sampling_rate=16000,
        return_tensors="pt"
    ).input_features

    input_features = input_features.to(device)

    # Generate transcription
    with torch.no_grad():

        predicted_ids = model.generate(
            input_features,
            max_length=225
        )

    # Convert token menjadi text
    transcription = processor.batch_decode(
        predicted_ids,
        skip_special_tokens=True
    )[0]

    return transcription


if __name__ == "__main__":

    audio_path = input(
        "Masukkan path audio: "
    )

    result = transcribe_audio(
        audio_path
    )

    print("\nHasil Transkripsi:")
    print(result)