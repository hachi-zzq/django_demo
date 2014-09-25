from django.db import models

class User(models.Model):
    username=models.CharField(max_length=256)
    password=models.CharField(max_length=200)
    email=models.CharField(max_length=200)

    def __unicode__(self):
        return self.username

class Comment(models.Model):
    user=models.ForeignKey(User)
    content=models.TextField()
