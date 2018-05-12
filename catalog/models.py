from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.contrib.auth.models import User # used to connect user to story

class Story(models.Model):
    """
    Model representing the story
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this story")
    title = models.CharField(max_length = 40, help_text = "Story Title")
    story = models.TextField(max_length = 3000, help_text = "Please tell us why people are awesome")
    Date_added = models.DateField(auto_now_add = True, null=True, blank=True)
    photo = models.ImageField(upload_to = 'image')
    Author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    featured = models.BooleanField( default = False, blank=True)
    photo_height = models.CharField( max_length = 8, help_text = "height of photo")
    photo_width = models.CharField( max_length = 8, help_text = "height of photo")
    top = models.CharField( max_length = 20, help_text = "center of the photo")
    left = models.CharField( max_length = 20, help_text = "center of the photo")
    # orientation = models.CharField( max_length = 2, help_text = "photo orientation") heroku test

    #Returns a string representing the model
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular Story
        """
        return reverse('story-detail', args=[str(self.id)])

class Product(models.Model):
    """
    Model representing products
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this product")
    name = models.CharField(max_length = 40, help_text = "Name of the product")
    price = models.DecimalField(max_digits = 5, decimal_places = 2, help_text = "price of product")
    photo = models.ImageField( upload_to = 'image\product', null=False, blank = False )
    description = models.TextField(max_length = 1000, help_text = "Description of the product")
    checkout_button = models.CharField(max_length = 40, null = True, help_text = "variable to hold paypal button")

    #Return a string representing the model
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular product
        """
        return reverse('product-detail', args=[str(self.id)])
