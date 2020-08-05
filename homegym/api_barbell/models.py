from django.db import models

# Create your models here.
class Barbell(models.Model):
  name = models.CharField(primary_key=True, unique=True, max_length=100)
  photo = models.CharField(max_length=100)
  link = models.CharField(max_length=100)
  brand = models.CharField(max_length=50)
  price = models.CharField(max_length=10)
  category = models.CharField(max_length=10)
  condition = models.CharField(max_length=10)
  available = models.BooleanField()
  updated_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'barbell'