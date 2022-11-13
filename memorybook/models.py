from django.db import models



class Memory(models.Model):
    
    note = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note

