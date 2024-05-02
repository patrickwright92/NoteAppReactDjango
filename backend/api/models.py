from django.db import models
from django.contrib.auth.models import User

# Object Relational Mapping for our database
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto populate time
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')


    def __str__(self):
        return self.title