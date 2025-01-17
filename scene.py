from manim import *

class LetterByLetter(Scene):
    def construct(self):
        text = "Human-like writing"
        for i, char in enumerate(text):
            letter = Text(char)
            self.play(Write(letter), run_time=0.2 + i * 0.05)
            self.add(letter)  # Keep letters on screen
        self.wait()
