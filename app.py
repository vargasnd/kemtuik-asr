import gradio as gr
import tempfile

from inference import transcribe_audio

# ==========================================
# FUNCTION
# ==========================================


def transcribe(audio_path):

    if audio_path is None:
        return "", "Silakan upload atau rekam audio terlebih dahulu."

    try:
        result = transcribe_audio(audio_path)

        if not result.strip():
            return "", "Tidak ada teks yang terdeteksi."

        return result, "Transkripsi berhasil."

    except Exception as e:
        return "", f"Terjadi error: {str(e)}"


def clear_all():
    return None, None, "", "Menunggu audio..."


def create_txt(text):
    if not text or not text.strip():
        return None

    temp_file = tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="utf-8"
    )

    temp_file.write(text)
    temp_file.close()

    return temp_file.name


# ==========================================
# CUSTOM CSS
# ==========================================

css = """
#title {
    text-align: center;
    margin-bottom: 5px;
}

#subtitle {
    text-align: center;
    margin-bottom: 25px;
}

#transcribe-btn {
    height: 50px;
    font-size: 17px;
    font-weight: bold;
}

#clear-btn {
    height: 50px;
}

#status {
    text-align: center;
}

footer {
    display: none !important;
}
"""


# ==========================================
# INTERFACE
# ==========================================

with gr.Blocks(title="Kemtuik Speech to Text") as app:

    # HEADER
    gr.Markdown("""
        <h1 id="title">Kemtuik Speech to Text</h1>

        <p id="subtitle">
        Automatic Speech Recognition untuk Bahasa Kemtuik
        </p>
        """)

    # MAIN CONTENT
    with gr.Row():

        # ==================================
        # LEFT SIDE - INPUT
        # ==================================

        with gr.Column(scale=1):

            gr.Markdown("### Input Audio")

            audio_input = gr.Audio(
                sources=["upload", "microphone"],
                type="filepath",
                label="Upload atau Rekam Audio",
            )

            gr.Markdown("""
                **Format yang didukung:** WAV, MP3, FLAC,
                dan format audio umum lainnya.
                """)

            with gr.Row():

                transcribe_button = gr.Button(
                    "Transkripsikan", variant="primary", elem_id="transcribe-btn"
                )

                clear_button = gr.Button("Clear", elem_id="clear-btn")

        # ==================================
        # RIGHT SIDE - OUTPUT
        # ==================================

        with gr.Column(scale=1):

            gr.Markdown("### Hasil Transkripsi")

            output_text = gr.Textbox(
                label="Hasil Transkripsi",
                lines=5,
                placeholder="Hasil transkripsi akan muncul di sini...",
            )

            with gr.Row():
                status = gr.Markdown("Menunggu audio...", elem_id="status")

    # ==========================================
    # BUTTON ACTION
    # ==========================================

    transcribe_button.click(
        fn=transcribe, inputs=audio_input, outputs=[output_text, status]
    ).then(fn=lambda x: x, inputs=audio_input)

    clear_button.click(
        fn=clear_all,
        inputs=[],
        outputs=[audio_input, output_text, status],
    )

# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":
    app.launch(css=css, share=True)
