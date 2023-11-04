from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=57)
    email = models.EmailField()
    title = models.CharField(max_length=107)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
