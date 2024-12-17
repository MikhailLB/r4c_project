from django.db import models


class Customer(models.Model):
    email = models.CharField(max_length=255,blank=False, null=False)

    class Main:
        indexes = [
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return self.email