from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


class app_User(User):
    RegistrationDate = models.DateTimeField( auto_now_add=True, null=False)

class Video(models.Model):
    title = models.CharField( max_length=50, null=False, blank=False)
    description = models.TextField()
    uploadData = models.DateTimeField( auto_now_add=True, null=False)
    videoLink = models.URLField(max_length=2048)
    Rating = models.PositiveBigIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )

class Subscription(models.Model):
    userID = models.ForeignKey(app_User, on_delete= models.CASCADE , null= False)
    price = models.PositiveIntegerField()
    subscriptionType = models.CharField(max_length=300)
    Duration = models.DateTimeField(null=False)
    

class History(models.Model):
    videoID = models.ForeignKey("video", on_delete=models.CASCADE, null=False)
    userID = models.ForeignKey("app_User", on_delete=models.CASCADE, null= False)
    date = models.DateTimeField(auto_now= True , null= False)
    liked = models.PositiveBigIntegerField(default= 0 , null= False)
    disliked = models.PositiveBigIntegerField(default= 0 , null= False)
    coment = models.TextField(blank=False, null=True)
    
    
# Create your models here.
