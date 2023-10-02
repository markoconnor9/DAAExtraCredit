from django.db import models
from django.contrib.auth.models import User

# Create your models here.
<<<<<<< HEAD
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    availability = models.ManyToManyField(Shift)

    #user = models.OneToOneField(User, on_delete=models.CASCADE)

=======
>>>>>>> parent of b7daf4b (created a login page and a form page)
