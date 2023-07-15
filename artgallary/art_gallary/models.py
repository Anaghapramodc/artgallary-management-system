from django.contrib.auth.models import User
from django.db import models
from pyexpat import model

from django.urls import reverse


# Create your models here.
class artist_sell(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    Painting_name = models.CharField(max_length=100)
    mediam = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    description = models.TextField()
    artcode = models.CharField(max_length=100)
    price = models.FloatField(null=True, blank=True)
    image_url = models.ImageField(upload_to='pics/')
    art_available = models.BooleanField()
    i_am_not_robot = models.BooleanField(default=False)
    def __str__(self):
        return self.Painting_name

class Order(models.Model):
    product = models.ForeignKey(artist_sell, max_length=200, null=True, on_delete=models.SET_NULL)
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    painting_name = models.ManyToManyField(artist_sell)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


class CartItem(models.Model):
    painting_name = models.ForeignKey(artist_sell, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{ self.quantity} x {self.painting_name}'

    @property
    def total_price(self):
        return self.painting_name.price * self.quantity


class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Profile(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles', null=True, blank=True)
        id_no = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_ids', null=True, blank=True)
        category = models.ForeignKey(Category, related_name='profiles', on_delete=models.CASCADE)
        name = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        mobile_number = models.CharField(max_length=15)
        bio = models.TextField()
        image_url = models.ImageField(upload_to='pics')
        i_am_not_robot = models.BooleanField(default=False)

        def __str__(self):
            return self.name

class artworks(models.Model):
    artwork = models.CharField(max_length=200)
    team1 =models.CharField(max_length=200)
    team2 =models.CharField(max_length=200)
    team3 =models.CharField(max_length=200)
    team4 =models.CharField(max_length=200)
    team5 =models.CharField(max_length=200)
    team6 =models.CharField(max_length=200)
    team7 =models.CharField(max_length=200)
    team8 =models.CharField(max_length=200)
    def __str__(self):
        return self.artwork

class compitition(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    feedback = models.TextField()
    image_url = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name

class Buy(models.Model):
    painting = models.ForeignKey('artist_sell', on_delete=models.CASCADE, related_name='buy_paintings', null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name', null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=15)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200)
    address_3 = models.CharField(max_length=200)
    pin = models.CharField(max_length=6)
    nearest_city = models.CharField(max_length=200)
    online_payment = models.BooleanField(default=False)
    cash_on_delivery = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class contact_us(models.Model):
    name = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    message = models.TextField()






