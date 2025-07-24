import os
import gradio as gr
from text_tools import (
    applica_dizionario_fn,
    inserisci_pause_fn,
    vai_a_capo_fn
)

SPEAKER_DIR = "speaker_previews"

def build_interface(genera_audio_fn, imposta_testo_fn, reset_testo_fn):
    with gr.Blocks(title="Studio Vocale Liturgico") as demo:
        gr.Markdown("## 🎙️ Studio Vocale Liturgico")

        testo_originale = gr.State("")

        with gr.Row():
            file_input = gr.File(label="📂 File .txt", type="filepath")
            testo_box = gr.Textbox(label="📝 Testo", lines=8)
            file_input.change(fn=lambda p: open(p, "r", encoding="utf-8").read() if p else "", inputs=[file_input], outputs=[testo_box])

        with gr.Row():
            imposta_btn = gr.Button("📥 Imposta")
            diz_btn = gr.Button("🕯️ Dizionario")
            pause_btn = gr.Button("⏸️ Pause")
            capo_btn = gr.Button("↵ A capo")

            imposta_btn.click(fn=imposta_testo_fn, inputs=[testo_box], outputs=[testo_originale])
            diz_btn.click(fn=applica_dizionario_fn, inputs=[testo_box], outputs=[testo_box])
            pause_btn.click(fn=inserisci_pause_fn, inputs=[testo_box], outputs=[testo_box])
            capo_btn.click(fn=vai_a_capo_fn, inputs=[testo_box], outputs=[testo_box])

        with gr.Row():
            reset_btn = gr.Button("🧼 Reset Testo")
            reset_btn.click(fn=reset_testo_fn, outputs=[testo_box])

        with gr.Row():
            speaker = gr.Dropdown(label="🎤 Voce", choices=[
                f.replace(".wav", "") for f in os.listdir(SPEAKER_DIR) if f.endswith(".wav")
            ])
            speaker_audio = gr.Audio(label="🔊 Anteprima Voce", interactive=False)
            speaker.change(
                fn=lambda s: os.path.join(SPEAKER_DIR, f"{s}.wav") if os.path.exists(os.path.join(SPEAKER_DIR, f"{s}.wav")) else None,
                inputs=[speaker],
                outputs=[speaker_audio]
            )

        with gr.Row():
            nome = gr.Textbox(label="📄 Nome", value="salmo")
            formato = gr.Radio(label="🎼 Formato", choices=["wav", "mp3"], value="mp3")
            cartella = gr.Textbox(label="📁 Cartella", value="salmi")
            salva_file = gr.Checkbox(label="💾 Salva", value=True)

        genera_btn = gr.Button("🎧 Genera Audio")
        audio_output = gr.Audio(label="🔉 Risultato", interactive=False)
        messaggio = gr.Markdown()

        genera_btn.click(
            fn=genera_audio_fn,
            inputs=[testo_box, speaker, formato, nome, cartella, salva_file],
            outputs=[audio_output, messaggio]
        )

    return demo
