from django.contrib.auth.models  import Permission, User
from django.db import models

class Inverstor(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    amount = models.IntegerField()
    location = models.CharField(max_length=250)
    interest_rate = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.amount} - {self.interest_rate}"
