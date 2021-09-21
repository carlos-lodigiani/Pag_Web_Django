from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    name_of_books = models.CharField(max_length=15)
    name_of_user = models.CharField(max_length=30)
    description = models.TextField()
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    begin_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='media')
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)




