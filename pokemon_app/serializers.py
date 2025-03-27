from rest_framework import serializers # import serializers from DRF
from .models import Pokemon # import Pokemon model from models.py

class PokemonSerializer(serializers.ModelSerializer):
    moves =serializers.SerializerMethodField()

    class Meta:
        model = Pokemon # specify what model this serializer is for
        fields = ['id', 'name', 'level'] # specify the fields you would like this serializer to return. 
        # Alternatively if you would like to cover all fields at once you could use "__all__" within the fields list.

    def get_moves(self, instance):
        moves = instance.moves.all()
        move_names = [move.name for move in moves]
        return move_names