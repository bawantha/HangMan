from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Game


class GameAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_new_game(self):
        response = self.client.post('/game/new')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)

    def test_guess_correct(self):
        game = Game()
        game.word = "python"
        game.max_incorrect_guesses = len(game.word) - 1
        game.save()

        response = self.client.post(f'/game/{game.id}/guess', {"guess": "p"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["correct"])

    def test_guess_incorrect(self):
        game = Game()
        game.word = "python"
        game.max_incorrect_guesses = len(game.word) - 1
        game.save()

        response = self.client.post(f'/game/{game.id}/guess', {"guess": "z"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data["correct"])
