from django.db import models


class Chat(models.Model):

    id = models.PositiveIntegerField(primary_key=True, unique=True)
    counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id)


