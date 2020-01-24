from django.db import models


class Banks(models.Model):
    ifsc_code = models.TextField(db_index=True)
    bank_id = models.PositiveIntegerField()
    branch = models.TextField()
    address = models.TextField()
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)

