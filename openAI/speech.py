import openai
import sounddevice as sd
import soundfile as sf
import numpy as np
from scipy.io.wavfile import write
import tempfile
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

SAMPLE_RATE = 16000
DURATION = 6  # sekundy nagrania

def record_audio():
    print("🎤 Mów...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE),
                    samplerate=SAMPLE_RATE,
                    channels=1,
                    dtype="int16")
    sd.wait()
    print("⏹️ Koniec nagrania")
    return audio

def speech_to_text(audio):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        write(f.name, SAMPLE_RATE, audio)

        with open(f.name, "rb") as audio_file:
            transcript = openai.audio.transcriptions.create(
                file=audio_file,
                model="whisper-1",
                language="pl"
            )

    os.unlink(f.name)
    return transcript.text

def chat_response(text):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Jesteś pomocnym asystentem i odpowiadasz po polsku."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

def text_to_speech(text):
    speech = openai.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text
    )

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        f.write(speech.read())
        filename = f.name

    data, sr = sf.read(filename)
    sd.play(data, sr)
    sd.wait()
    os.unlink(filename)

def main():
    while True:
        audio = record_audio()
        text = speech_to_text(audio)
        print("📝 Ty:", text)

        if text.lower() in ["koniec", "stop", "wyjście"]:
            break

        answer = chat_response(text)
        print("🤖 AI:", answer)
        text_to_speech(answer)

if __name__ == "__main__":
    main()
