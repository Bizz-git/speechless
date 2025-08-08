import speech_recognition as sr

def riconosci_audio():
    """
    Cattura l'audio dal microfono e lo converte in testo.
    """
    # Crea un oggetto Recognizer
    r = sr.Recognizer()

    # Utilizza il microfono come sorgente audio
    with sr.Microphone() as source:
        print("In ascolto... Parla ora!")
        # Regola il recognizer per il rumore ambientale
        r.adjust_for_ambient_noise(source)
        # Ascolta l'audio dal microfono
        audio = r.listen(source)

    try:
        # Prova a riconoscere il parlato usando l'API di Google
        testo = r.recognize_google(audio, language='it-IT')
        print(f"Hai detto: {testo}")
    except sr.UnknownValueError:
        # Errore: il motore di riconoscimento non ha capito l'audio
        print("Non è stato possibile capire l'audio.")
    except sr.RequestError as e:
        # Errore: impossibile connettersi all'API di Google
        print(f"Errore nella richiesta al servizio di Google Speech Recognition; {e}")

if __name__ == "__main__":
    riconosci_audio()
