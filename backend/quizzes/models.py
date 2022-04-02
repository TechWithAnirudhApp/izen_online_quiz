from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class Quiz(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=255, default='')
	topic = models.CharField(max_length=120, default='')
	time = models.IntegerField(help_text="duration of the quiz in minutes")
	required_score_to_pass = models.IntegerField(help_text="required score in %", default=50)
	difficluty = models.CharField(max_length=6, choices=DIFF_CHOICES)
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
	# created_at = models.DateTimeField(auto_now_add=True)

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
	# user = models.ForeignKey(User, on_delete=models.CASCADE)
	user = models.CharField(max_length=255, default='User')
	score = models.DecimalField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)], max_digits=5, decimal_places=2)

	class Meta:
		ordering = ['id']

	def __str__(self):
	    return str(self.pk)

class Answer(models.Model):
	question = models.ForeignKey(
		Question, 
		related_name='answers', 
		on_delete=models.CASCADE
	)
	text = models.CharField(max_length=255)
	correct = models.BooleanField(default=False)
	# created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text
