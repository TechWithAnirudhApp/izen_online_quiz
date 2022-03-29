from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=255, default='')
	created_at = models.DateTimeField(auto_now_add=True)
	times_taken = models.IntegerField(default=0, editable=False)

	@property
	def question_count(self):
		return self.questions.count()
	
	class Meta:
		verbose_name_plural = "Quizzes"
		ordering = ['id']

	def __str__(self):
		return self.title

class Question(models.Model):
	quiz = models.ForeignKey(
		Quiz, 
		related_name='questions', # need related name for hyper link related field to work ?!?
		on_delete=models.CASCADE
	)
	prompt = models.CharField(max_length=255, default='')

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.prompt

class Result(models.Model):
	quiz = models.ForeignKey(
		Quiz, 
		related_name='results', # need related name for hyper link related field to work ?!?
		on_delete=models.CASCADE
	)
	score = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['id']

	def __int__(self):
		return self.score

class Answer(models.Model):
	question = models.ForeignKey(
		Question, 
		related_name='answers', 
		on_delete=models.DO_NOTHING
	)
	text = models.CharField(max_length=255)
	correct = models.BooleanField(default=False)

	def __str__(self):
		return self.text
