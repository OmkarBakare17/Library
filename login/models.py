from django.db import models

# Create your models here.
class User_signup(models.Model):
    name = models.CharField(max_length=30)
    mail = models.EmailField()
    password = models.CharField(max_length=30)

    class Meta:
        db_table = 'login'