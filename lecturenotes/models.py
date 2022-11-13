from django.db import models

# Create your models here.

class lectureCode(models.Model):
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code

class lectureNote(models.Model):
    code = models.ForeignKey(lectureCode, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.title
    