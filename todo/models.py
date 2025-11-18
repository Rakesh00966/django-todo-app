# todo/models.py
from django.db import models 
from django.contrib.auth.models import User

class TODOO(models.Model):
    srno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=201)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)   # <-- new field

    def __str__(self):
        return f"{self.srno} - {self.title}"
