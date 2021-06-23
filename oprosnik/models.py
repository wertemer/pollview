from django.db import models

class Opros(models.Model):
	id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=255,default='',editable=True)
	date_begin=models.DateTimeField()
	date_end=models.DateTimeField()
	desc=models.TextField(default='',editable=True)
	class ReadonlyMeta:
		readonly = ["date_begin"]

class Questions(models.Model):
	TEXT=1
	SELECT_VAR=2
	MULTI_SELECT_VAR=3
	QUESTION_ANS_TYPE_CHOICES=(
		(TEXT,'Текст'),
		(SELECT_VAR,'Выбор варианта'),
		(MULTI_SELECT_VAR,'Множественный выбор'),
	)
	id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=255,null=False)
	type=models.IntegerField(choices=QUESTION_ANS_TYPE_CHOICES,default=TEXT)
	f_opros=models.ForeignKey('Opros',on_delete=models.CASCADE,default=None)

class Answers(models.Model):
	id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=255,null=False)
	f_questions=models.ForeignKey('Questions',on_delete=models.CASCADE)

class Users(models.Model):
	id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=255,default='Аноним')

class UserAnswers(models.Model):
	f_user=models.ForeignKey('Users',on_delete=models.CASCADE)
	f_answer=models.ForeignKey('Answers',on_delete=models.CASCADE)
