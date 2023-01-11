from django.db import models

# Create your models here.


class Job(models.Model):

    type = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=1)
    url = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.type} -> {self.title} -> {self.description}"


class Log(models.Model):

    action_choices = (('created', 'created'),
                      ('updated', 'updated'),
                      ('refresh', 'refresh'))

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=action_choices)
    url = models.CharField(max_length=100)
