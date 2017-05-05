from rest_framework import serializers

from .models import Album


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        # fields = ('ticker', 'volume')
        fields = '__all__'
