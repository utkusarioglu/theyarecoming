from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.


class Story(models.Model):
    class Meta:
        verbose_name_plural = "Stories"

    title = models.CharField(max_length=200, default="")
    body = models.TextField(max_length=2000)
    pub_date = models.DateField("publish date")

    def __str__(self):
        return self.title

    def save(self):
        if not self.id:
            self.pub_date = datetime.today()
        super(Story, self).save()


class Choice(models.Model):
    body = models.CharField(max_length=200)
    host_story = models.ForeignKey(
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

class ChoiceRecord(models.Model):
    host_story = models.ForeignKey(
        Story,
        on_delete=models.CASCADE,
        related_name="host_story_id"
    )
    next_story = models.ForeignKey(
        Story,
        on_delete=models.CASCADE,
        related_name="next_story_id"
    )
    pub_date = models.DateTimeField("Choice Datetime")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def save(self):
        if not self.id:
            self.pub_date = datetime.now()
        super(ChoiceRecord, self).save()