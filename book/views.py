from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Story

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