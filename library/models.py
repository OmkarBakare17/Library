from django.db import models

# Create your models here.
class add_book(models.Model):
    name = models.CharField(max_length=30)
    auther = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = 'book'