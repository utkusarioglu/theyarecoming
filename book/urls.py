from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:story_id>/", views.index, name="index"),
    path(r"story/<int:story_id>", views.StoryAPI.as_view(), name="api")
]
