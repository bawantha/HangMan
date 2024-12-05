from rest_framework import serializers

from .models import Game


class GameSerializer(serializers.ModelSerializer):
    current_word_state = serializers.SerializerMethodField()
    remaining_guesses = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ['id', 'state', 'current_word_state', 'incorrect_guesses', 'remaining_guesses']

    @staticmethod
    def get_current_word_state(obj):
        return obj.current_word_state()

    @staticmethod
    def get_remaining_guesses(obj):
        return obj.max_incorrect_guesses - obj.incorrect_guesses
