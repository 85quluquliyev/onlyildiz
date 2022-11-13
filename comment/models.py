from django.db import models
from django.forms import URLField



class allLink(models.Model):
    
    link = models.URLField()

    def __str__(self):
        return self.link

class allComment(models.Model):

    link = models.ForeignKey(allLink, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    bad = models.BooleanField(default=False)
    confirm = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
