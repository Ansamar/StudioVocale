def imposta_testo_di_partenza_fn(testo_corrente):
    """Imposta il testo attuale come riferimento per i reset."""
    return testo_corrente

def reset_totale_fn():
    """Cancella tutto il contenuto del textbox."""
    return ""

def applica_dizionario_fn(testo):
    """Corregge termini liturgici noti usando un dizionario."""
    vocabolario = {
        "alleluja": ["Alleluia"],
        "agnus dei": ["Agnus Dei"],
        "kyrie": ["Kýrie"],
        "gloria": ["Gloria"],
        "sanctus": ["Sanctus"],
        "miserere": ["Miserére"]
    }
    for parola, varianti in vocabolario.items():
        corretto = varianti[0]
        testo = testo.replace(parola.lower(), corretto)
    return testo

def inserisci_pause_fn(testo):
    """Inserisce pause simboliche nel testo per migliorare la dizione."""
    return (testo
            .replace(".", " —")
            .replace("«", "—")
            .replace("»", "—")
            .replace("!", " —")
            .replace("?", " —"))

def vai_a_capo_fn(testo):
    """Inserisce interruzioni di riga dopo i punti per leggibilità."""
    return testo.replace(".", ".\n")
