from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator



class Video(models.Model):
    title = models.CharField( max_length=50, null=False, blank=False)
    description = models.TextField()
    upload_data = models.DateTimeField( auto_now_add=True, null=False)
    # videoLink = models.URLField(max_length=2048)
    Rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )
    
    def __str__(self):
        return self.title

class Subscription(models.Model):
    PENDING = 'pending'
    ACTIVE = 'active'
    EXPIRED = 'expired'

    PAYMENT_STATUS_CHOICES = [
        (ACTIVE, 'Paid'),
        (PENDING, 'Not Paid'),
        (EXPIRED, 'Expired'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    subscription_type = models.CharField(max_length=300)
    duration = models.DurationField(null=False)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default=PENDING)
    payment_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.subscription_type}'

    

class History(models.Model):
    video = models.ForeignKey(Video , on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User , on_delete=models.CASCADE, null= False)
    date = models.DateTimeField(auto_now= True , null= False)
    liked = models.PositiveIntegerField(default= 0 , null= False)
    disliked = models.PositiveIntegerField(default= 0 , null= False)
    comment = models.TextField(blank=False, null=True)
    
    def __str__(self):
        return f'History of {self.user.username} watching {self.video.title}'
    
    
# Create your models here.
