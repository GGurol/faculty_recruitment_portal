# models.py

from django.db import models

class UserRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    category = models.CharField(max_length=10, choices=[('GEN', 'GEN'), ('EWS', 'EWS'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'), ('PWD', 'PWD')])
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
