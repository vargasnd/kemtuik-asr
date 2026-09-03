# Kemtuik Speech-to-Text

Prototype sistem Automatic Speech Recognition (ASR) untuk mentranskripsikan suara Bahasa Kemtuik menjadi teks menggunakan Whisper Small yang telah di-fine-tuning.

## Teknologi

- Python
- PyTorch
- Hugging Face Transformers
- Whisper Small
- Librosa
- Gradio

## Dataset

Dataset terdiri dari 3.957 audio sintetis Bahasa Kemtuik:

- Training: 3.165
- Validation: 396
- Testing: 396
- Speaker laki-laki: 1.980
- Speaker perempuan: 1.977

## Hasil Evaluasi

| Metric         |  Hasil |
| -------------- | -----: |
| Validation WER | 17,54% |
| Test WER       | 24,91% |
| Test CER       |  9,00% |

## Model

Model hasil fine-tuning disimpan di Hugging Face Model Hub:

**https://huggingface.co/vargasnd/kemtuik-whisper-small**

Model akan diunduh secara otomatis saat pertama kali aplikasi dijalankan.

## Install Dependency

Buat dan aktifkan virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install semua library yang dibutuhkan:

```bash
pip install -r requirements.txt
```

## Jalankan Aplikasi

```bash
python app.py
```

Buka link yang muncul di terminal pada browser.

> Pada pertama kali dijalankan, model akan diunduh otomatis dari Hugging Face. Pastikan komputer terhubung ke internet.
