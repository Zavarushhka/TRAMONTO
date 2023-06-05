from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    nickname = models.CharField("Nickname", max_length=20)
    password = models.CharField("Password", max_length=40)
    points = models.IntegerField("Points", default=0)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "User"

class Order(models.Model):
    name = models.CharField("Name", max_length=20)
    email = models.EmailField("Email", max_length=50 )
    phone = models.CharField("Phone", max_length=20)

    def __str__(self):
        data = self.name + ' ' + self.phone
        return data
    
    class Meta:
        verbose_name = "Name"

class LikeBlock(models.Model):
    liked = models.ManyToManyField(User, default=None, blank=True)
    
    
    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_block = models.ForeignKey(LikeBlock, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)