from rest_framework import serializers
from .models import Move

class MoveSerializer(serializers.ModelSerializer):
    pokemon = serializers.SerializerMethodField()
    
    class Meta:
        model = Move
        fields = "__all__"

    def get_pokemon(self, obj):
        pokemon = obj.pokemon.all()
        pokemon = [pkmn.name for pkmn in pokemon]
        return pokemon