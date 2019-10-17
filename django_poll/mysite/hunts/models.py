import datetime

from django.db import models
from django.utils import timezone

class HuntClue(models.Model):
    clue_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.clue_text


class ClueAnswer(models.Model):
    clue = models.ForeignKey(HuntClue, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
       return self.answer_text