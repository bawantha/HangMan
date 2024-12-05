import random

from django.db import models

WORDS = ["Hangman", "Python", "Audacix", "Bottle", "Pen"]


class Game(models.Model):
    word = models.CharField(max_length=100)
    state = models.CharField(
        max_length=10,
        choices=[("InProgress", "InProgress"), ("Lost", "Lost"), ("Won", "Won")],
        default="InProgress",
    )
    incorrect_guesses = models.IntegerField(default=0)
    max_incorrect_guesses = models.IntegerField()
    guessed_letters = models.TextField(default="")  # Store letters guessed so far

    def initialize(self):
        """Initialize a new game with a random word and calculate max incorrect guesses."""
        self.word = random.choice(WORDS).lower()
        self.max_incorrect_guesses = len(self.word) - 1
        self.save()

    def current_word_state(self):
        """Generate the current word state with guessed letters."""
        return ''.join([char if char in self.guessed_letters else '_' for char in self.word])

    def update_state(self, guess):
        """Update game state based on the guess."""
        if guess in self.word and guess not in self.guessed_letters:
            self.guessed_letters += guess
        elif guess not in self.word:
            self.incorrect_guesses += 1

        if set(self.word).issubset(set(self.guessed_letters)):
            self.state = "Won"
        elif self.incorrect_guesses > self.max_incorrect_guesses:
            self.state = "Lost"
        else:
            self.state = "InProgress"
        self.save()
