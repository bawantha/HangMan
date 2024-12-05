from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Game
from .serializers import GameSerializer


class NewGameView(APIView):
    @staticmethod
    def post(request):
        """Create a new game."""
        game = Game()
        game.initialize()
        return Response({"id": game.id}, status=status.HTTP_201_CREATED)


class GameStateView(APIView):
    @staticmethod
    def get(request, id):
        """Retrieve the state of a game."""
        try:
            game = Game.objects.get(id=id)
        except Game.DoesNotExist:
            return Response({"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GuessView(APIView):
    @staticmethod
    def post(request, id):
        """Handle a guess and return the updated game state."""
        try:
            game = Game.objects.get(id=id)
        except Game.DoesNotExist:
            return Response({"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND)

        if game.state != "InProgress":
            return Response({"error": "Game is already over"}, status=status.HTTP_400_BAD_REQUEST)

        guess = request.data.get("guess", "").lower()
        if len(guess) != 1 or not guess.isalpha():
            return Response({"error": "Invalid guess. Provide a single letter."}, status=status.HTTP_400_BAD_REQUEST)

        game.update_state(guess)
        serializer = GameSerializer(game)
        return Response({"game_state": serializer.data, "correct": guess in game.word}, status=status.HTTP_200_OK)
