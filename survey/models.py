from django.db import models
from django.conf import settings

class Survey(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='surveys'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Survey({self.id}): {self.title}"


class Question(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    survey = models.ForeignKey(
        Survey, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='questions'
    )
    def __str__(self):
        return f"Question({self.id}): {self.text} - {self.survey}" 

class Choice(models.Model):
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(
        Question, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='choices'
    )

    def __str__(self):
        return f"Choice({self.id}): {self.text} - {self.question}"