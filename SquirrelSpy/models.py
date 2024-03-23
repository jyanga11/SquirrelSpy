from django.db import models
from django.contrib.auth.models import AbstractUser

class Squirrel(models.Model):
    name = models.CharField(max_length=30)
    weight = models.IntegerField()
    sex = models.CharField(max_length=10)
    age = models.IntegerField(default=1)
    species = models.CharField(max_length=20)
    serial_num = models.CharField(max_length=20)
    left_ear_color = models.CharField(max_length=30)
    right_ear_color = models.CharField(max_length=30)
    image = models.ImageField(upload_to='squirrel_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    # Fields in AbstractUser class
        # username
        # email
        # password
        # is_staff - default = False
        # is_active - default = True
        # date_joined - default = Datetime Created
    # Custom fields
    reliability = models.IntegerField(default=2)
    ranking = models.IntegerField(default=4)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)

    def __str__(self):
        return self.username

class Sighting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    squirrel = models.ForeignKey(Squirrel, on_delete=models.CASCADE, null=True)
    lat = models.FloatField()
    long = models.FloatField()
    time = models.DateTimeField()
    behavior = models.CharField(max_length=50)
    certainty_level = models.IntegerField(default=2)
    is_verified = models.BooleanField(default=False)
    verification_comment = models.CharField(null=True, max_length=50)
    image = models.ImageField(upload_to='sighting_images/', blank=True, null=True)

    def __str__(self):
        return self.squirrel.name + " - " + self.user.username