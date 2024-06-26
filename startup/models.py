from django.db import models

# Create your models here.


class Team(models.Model):
  name = models.CharField(max_length=120)
  designation = models.CharField(max_length=120)
  image = models.ImageField(default="default.jpg", upload_to='team_pics')
  twitter_link = models.URLField(blank=True, null=True)
  facebook_link = models.URLField(blank=True, null=True)
  instagram_link = models.URLField(blank=True, null=True)
  linkedin_link = models.URLField(blank=True, null=True)
  
  def __str__(self):
      return self.name
  


class Service(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  image = models.ImageField(default="default.jpg", upload_to='service_pics')
  
  def __str__(self):
      return self.title
  

class Testimonial(models.Model):
  client_name = models.CharField(max_length=120)
  profession = models.CharField(max_length=200)
  description = models.TextField()
  image = models.ImageField(default="default.jpg", upload_to='testimonial_pics')
  
  def __str__(self):
      return self.client_name
  