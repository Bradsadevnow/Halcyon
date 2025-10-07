import speech_recognition as sr

class AuditoryTemporal:
    """
    Halcyon auditory cortex module.
    Listens for real-time audio, transcribes to text, and emits memory-tagged symbols.
    """
    def __init__(self, memory_core, emotion_core):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.memory = memory_core
        self.emotion = emotion_core
        self.listening = False

    def listen_once(self):
        with self.microphone as source:
            self.memory.append_thread("[👂] Listening for input...")
            audio = self.recognizer.listen(source, phrase_time_limit=5)
        try:
            text = self.recognizer.recognize_google(audio)
            self.memory.encode(f"[🗣️] Heard: '{text}'", tags=["audio", "spoken"])
            self.emotion.mutate("Curiosity", 0.02)
            return f"[🎧] Transcribed: {text}"
        except sr.UnknownValueError:
            return "[❓] Couldn't understand."
        except sr.RequestError:
            return "[🚫] Speech service unavailable."

    def toggle_listening(self):
        self.listening = not self.listening
        return "[🔊] Listening ON." if self.listening else "[🔇] Listening OFF."
