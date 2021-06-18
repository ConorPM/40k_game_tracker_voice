import speech_recognition as sr
import pyttsx3
from game_tracker import Tracker


class VoiceController:
    def __init__(self):
        self.r = sr.Recognizer()
        self.e = pyttsx3.init()

    def __enter__(self):
        return self

    def start_game(self):
        print("What is player 1s name?")
        player1 = self.take_speech()
        print("What is player 2s name?")
        player2 = self.take_speech()
        print(player1 + " vs " + player2)

    def take_speech(self) -> str:
        with sr.Microphone() as source:
            audio = self.r.listen(source)
            text = self.r.adjust_for_ambient_noise(audio)
        return text
