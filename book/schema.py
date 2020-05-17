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
    story = graphene.Field(StoryType,
        id=graphene.Int(),
        title=graphene.String(),
        body=graphene.String(),
        pub_date=graphene.Date())
    all_stories = graphene.List(StoryType)
    choice = graphene.Field(ChoiceType,
        id=graphene.Int(),
        host_story=graphene.Int(),
        next_story=graphene.Int())
    all_choices = graphene.List(ChoiceType)

    def resolve_all_stories(self, info, **kwargs):
        return Story.objects.all()

    def resolve_all_choices(self, info, **kwargs):
        return Choice.objects.select_related("host_story").all()

    def resolve_story(self, info, **kwargs):
        id = kwargs.get("id")
        title = kwargs.get("title")
        # TODO pub date can be added here but it requires filter rather than get

        if id is not None:
            return Story.objects.get(pk=id)        
        
        if title is not None:
            return Story.objects.get(title=title)
        
        return None

    def resolve_choice(self, info, **kwargs):
        id = kwargs.get("id")
        host_story = kwargs.get("host_story")
        next_story = kwargs.get("next_story")

        if id is not None:
            return Choice.objects.get(pk=id)

        if host_story is not None:
            return Choice.objects.get(host_story=host_story)

        if next_story is not None:
            return Choice.objects.get(next_story=next_story)

        return None
