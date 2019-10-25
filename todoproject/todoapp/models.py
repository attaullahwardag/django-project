from django.db import models

# Create your models here.
class Todoitem(models.Model):
    content = models.CharField(max_length=555,unique=True)

    def __str__(self):
        return self.content

class Articles(models.Model):
    title = models.CharField(max_length=555)
    post = models.TextField()
