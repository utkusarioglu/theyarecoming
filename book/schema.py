import graphene
from graphene_django.types import DjangoObjectType
from .models import Story, Choice


class StoryType(DjangoObjectType):
    class Meta:
        model = Story

class ChoiceType(DjangoObjectType):
    class Meta:
        model = Choice

class Query(object):
    all_stories = graphene.List(StoryType)
    all_choices = graphene.List(ChoiceType)

    def resolve_all_stories(self, info, **kwargs):
        return Story.objects.all()

    def resolve_all_choices(self, info, **kwargs):
        return Choice.objects.select_related("host_story_id").all()