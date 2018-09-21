from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import PersonalSong


class PersonalSongType(DjangoObjectType):
    class Meta:
        model = PersonalSong

    interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    personalsongs = graphene.List(PersonalSongType)

    def resolve_personalnotes(self, info):
        user = info.context.user

        if user.is_anonymous:
            return PersonalSongModel.objects.none()
        else:
            return PersonalSongModel.objects.filter(user=user)


schema = graphene.Schema(query=Query)
