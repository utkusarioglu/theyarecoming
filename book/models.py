from django.db import models

# Create your models here.


class Story(models.Model):
    title = models.CharField(max_length=200, default="")
    body = models.CharField(max_length=2000)
    pub_date = models.DateField("publish date")

    def __str__(self):
        return self.title

class Choice(models.Model):
    body = models.CharField(max_length=200)
    story_id = models.ForeignKey(
        Story, 
        on_delete=models.CASCADE, 
        related_name="choices")
    next_story = models.ForeignKey(
        Story, 
        default=1,
        on_delete=models.CASCADE, 
        related_name="next_story")

    def __str__(self):
        return self.body
