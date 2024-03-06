from django.db import models



# Define your first model from here:
class User(models.Model):
    first_name = models.CharField(null = False, max_length = 30, default = 'John')
    last_name = models.CharField(null = False, max_length = 30, default ='Doe')
    dob = models.DateField (null = False)