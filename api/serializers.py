from rest_framework import serializers, viewsets
from .models import PersonalSong


class SongsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalSong
        fields = ('title', 'artist')

    def create(self, validated_data):
        user = self.context['request'].user
        song = PersonalSong.objects.create(user=user, **validated_data)
        return song


class SongsViewSet(viewsets.ModelViewSet):
    serializer_class = SongsSerializer
    queryset = PersonalSong.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return PersonalSong.objects.none()
        else:
            return PersonalSong.objects.filter(user=user)
