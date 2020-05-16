from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Story
from rest_framework import generics
from .serializers import StorySerializer

def index(request, story_id=1): 
    
    try:
        story = Story.objects.get(pk=story_id)
        choices = story.choices.all()
    except Story.DoesNotExist:
        raise(Http404("Story does not exist"))

    # substitions
    substitutions = [
        ("<<name>>", "John"),
    ]
    for find, replace in substitutions:
        story.body = story.body.replace(find, replace)
        for choice in choices:
            choice.body = choice.body.replace(find, replace) 

    content = {
        "story": story,
        "choices": choices,
    }
    return render(request, "book/index.html", content)

class StoryAPI(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def get_queryset(self):
        story_id = self.kwargs["story_id"]
        content = Story.objects.filter(pk=story_id)

        return content