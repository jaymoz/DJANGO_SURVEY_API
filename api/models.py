from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)

class Survey(models.Model):
	name = models.CharField(max_length=150,blank=True)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	description = models.TextField(max_length=700,blank=True)

	def __str__(self):
		return self.name

class SurveyQuestions(models.Model):
	question_choices = (
		('text','TEXT'),
		('multiple','MULTIPLE'),
		('radio','RADIO'),
	)
	survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='surv')
	survey_question_type = models.CharField(max_length=200,choices=question_choices)
	survey_question = models.CharField(max_length=500)

	class Meta:
		verbose_name = 'Survey Question'
		verbose_name_plural = 'Survey Questions'


	def save(self, *args, **kwargs):
		if (self.survey_question_type == 'TEXT' or self.survey_question_type == 'MULTIPLE' 
			or self.survey_question_type == 'RADIO'):
			values = self.question_choices.split()
			if len(values < 2):
				raise ValidationError("Question Choices cannot be one item")
		super(SurveyQuestions, self).save(*args, **kwargs)

	def __str__(self):
		return self.survey_question

class Choice(models.Model):
	question = models.ForeignKey(SurveyQuestions, on_delete=models.CASCADE)
	text = models.CharField(max_length=500)

class UserResponse(models.Model):
	user_id = models.IntegerField()
	survey = models.ForeignKey(Survey, on_delete=models.PROTECT,related_name='response_surv')
	survey_question = models.ForeignKey(SurveyQuestions,on_delete = models.PROTECT, related_name='survey_options_res')
	user_answer = models.CharField(max_length=500, default='')
	choice = models.ForeignKey(Choice, on_delete=models.CASCADE,null=True,default='')

	def __str__(self):
		return self.survey.name
