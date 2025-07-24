import os
import subprocess
from interface import build_interface
from text_tools import (
    applica_dizionario_fn,
    inserisci_pause_fn,
    vai_a_capo_fn,
    imposta_testo_di_partenza_fn,
    reset_totale_fn
)

SPEAKER_DIR = "speaker_previews"

def genera_audio(testo, speaker, formato, nome, cartella, salva_file):
    if not testo.strip():
        return None, "❌ Testo vuoto."

    # ✨ Applica trasformazioni testuali
    testo = applica_dizionario_fn(testo)
    testo = inserisci_pause_fn(testo)
    testo = vai_a_capo_fn(testo)

    # 🔊 Verifica voce
    speaker_path = os.path.join(SPEAKER_DIR, f"{speaker}.wav")
    if not os.path.exists(speaker_path):
        return None, f"❌ Voce non trovata: {speaker}"

    # 🎙️ Comando TTS
    comando = [
        "tts",
        "--model_name", "tts_models/multilingual/multi-dataset/xtts_v2",
        "--text", testo,
        "--speaker_wav", speaker_path,
        "--language_idx", "it",
        "--out_path", "output.wav"
    ]

    try:
        subprocess.run(comando, check=True)

        if salva_file:
            os.makedirs(cartella, exist_ok=True)
            destinazione = os.path.join(cartella, f"{nome}.{formato}")
            os.rename("output.wav", destinazione)
            return destinazione, f"💾 Audio salvato in: {destinazione}"
        else:
            return "output.wav", "🎧 Anteprima generata (non salvata)"
    except Exception as e:
        return None, f"❌ Errore generazione audio: {e}"

if __name__ == "__main__":
    demo = build_interface(genera_audio, imposta_testo_di_partenza_fn, reset_totale_fn)
    demo.launch()
