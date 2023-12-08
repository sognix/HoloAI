from pydub import AudioSegment
from pydub.playback import play
import vosk
import wave
import os
from datetime import datetime

def debug(output):
    print(str(datetime.now()) + ':    ' + output)

def write_to_txt(transcription, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(transcription)

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Die Datei {file_path} wurde erfolgreich gelöscht.")
    except OSError as e:
        print(f"Fehler beim Löschen der Datei {file_path}: {e}")

def convert_mp3_to_wav(mp3_file, wav_file, sample_rate=16000, channels=1, sample_width=2):
    # Öffnet die MP3-Datei mit pydub
    audio = AudioSegment.from_file(mp3_file, format="mp3")

    # Konvertiert das Audioformat
    audio = audio.set_frame_rate(sample_rate)
    audio = audio.set_channels(channels)
    audio = audio.set_sample_width(sample_width)

    # Speichert das Audio als WAV-Datei
    audio.export(wav_file, format="wav")

def audio_to_text(audio_path, model_path):
 # Lade das Vosk-Modell
    vosk_model = vosk.Model(model_path)

    # Öffne das Audiofile
    audio_file = wave.open(audio_path, "rb")

    # Erstelle einen Vosk-Recognizer mit dem geladenen Modell
    rec = vosk.KaldiRecognizer(vosk_model, audio_file.getframerate())

    # Lese den Inhalt des Audiofiles
    while True:
        data = audio_file.readframes(4000)  # Lese 4000 Frames auf einmal
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()

    # Überprüfe, ob es noch nicht akzeptierte Daten gibt
    result += rec.FinalResult()

    # Gib die Transkription aus
    return result



if __name__ == "__main__":
    mp3_file = "TrainingData/Audio/MP3/s01e1.mp3"
    wav_file = "TrainingData/Audio/WAV/s01e1.wav"
    model_path = "PrepareData/Model/vosk-model-de-0.21"
    output_path = "TrainingData/Transcription/Audio2Text/s01e1.txt"

    debug("CONVERT MP3 TO WAV")
    convert_mp3_to_wav(mp3_file, wav_file)

    debug("CONVERT WAV TO TXT")
    transcription = audio_to_text(wav_file, model_path)
    write_to_txt(transcription, output_path)

    debug("DELETE WAV")
    delete_file(wav_file)
