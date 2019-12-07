import datetime

from django.db import models
from django.utils import timezone
# for quiz
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

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

class Hunt(models.Model):
	name = models.CharField(max_length=1000)
	stops_count = models.IntegerField(default=0)
	description = models.CharField(max_length=70)
	created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	slug = models.SlugField()
	roll_out = models.BooleanField(default=False)
	def __str__(self):
		return self.name

class Meta:
	ordering = ['created',]
	verbose_name_plural ="Hunts"

	def __str__(self):
		return self.name

class Stop(models.Model):
	hunt = models.ForeignKey(Hunt, on_delete=models.CASCADE)
	label = models.CharField(max_length=1000)
	order = models.IntegerField(default=0)

	def __str__(self):
		return self.label
class Answer(models.Model):
	stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
	text = models.CharField(max_length=1000)
	is_correct = models.BooleanField(default=False)
	
	def __str__(self):
		return self.text

class Usrs(models.Model):
	#usr = models.ForeignKey(User, on_delete=models.CASCADE)
	hunt = models.ForeignKey(Hunt, on_delete=models.CASCADE)
	usr = models.CharField(max_length=250,default="")
	correct_answers = models.IntegerField(default=0)
	correct = models.CharField(max_length=500,default="")
	completed = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.usr

class Corrects(models.Model):
	usrs = models.ForeignKey(Usrs, on_delete=models.CASCADE)
	correct = models.CharField(max_length=500, default="")
	def __str__(self):
		return self.correct

class Response(models.Model):
	usr = models.ForeignKey(Usrs, on_delete=models.CASCADE)
	stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer,on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return self.stop.label
	@receiver(post_save, sender=Hunt)
	def set_default_hunt(sender, instance, created,**kwargs):
		hunt = Hunt.objects.filter(id = instance.id)
		hunt.update(stops_count=instance.stop_set.filter(hunt=instance.pk).count())

	@receiver(post_save, sender=Stop)
	def set_default(sender, instance, created,**kwargs):
		hunt = Hunt.objects.filter(id = instance.hunt.id)
		hunt.update(stops_count=instance.hunt.stop_set.filter(hunt=instance.hunt.pk).count())

	@receiver(pre_save, sender=Hunt)
	def slugify_title(sender, instance, *args, **kwargs):
		instance.slug = slugify(instance.name)