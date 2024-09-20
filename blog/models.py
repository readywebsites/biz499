
from enum import unique
from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from autoslug import AutoSlugField


class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    description = models.TextField()
    pic = models.ImageField(upload_to='new_media/')
    
    def __str__(self):
      return self.name

class Category (models.Model):
  title = models.CharField(max_length=20)

  def __str__(self):
    return self.title

class Hashtags (models.Model):
  tag = models.CharField(max_length=20)


class Blog_Post(models.Model):
  title = models.CharField(max_length=100)
  overview = models.TextField(max_length=400)
  Description =HTMLField()
  Timestamp = models.DateTimeField(auto_now_add= True)
  publish_date = models.DateField()
  author = models.ForeignKey(Team, on_delete=models.CASCADE)
  thumbnail_1620_720 = models.ImageField(upload_to='new_media/')
  square_small_thumbnail_200_200 = models.ImageField(upload_to='new_media/')
  categories = models.ManyToManyField(Category)
  hashtags = models.ManyToManyField(Hashtags,blank=True)
  # project = models.BooleanField()
  meta_description = models.CharField(max_length=100, blank=True)
  meta_keywords = models.CharField(max_length=1000,blank=True)
  meta_title = models.CharField(max_length=100, blank=True)
  meta_author = models.CharField(max_length=100, blank=True)
  new_blog_slug = AutoSlugField(populate_from='title',unique=True, null=True, default=None )
  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post',kwargs={
      'slug':self.new_blog_slug
    })
  def __str__(self):
    return self.title

class Pricecard(models.Model):
    title = models.CharField(max_length=200)
    features_included = models.CharField(max_length=200)
    features_excluded = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    
    def features_included_list(self):
      # return list(self.features_included)
      return self.features_included.split(',')
      
    def features_excluded_list(self):
      return self.features_excluded.split(',')

    def __str__(self):
      return self.title

# Portfolio

class Project_Strategy(models.Model):
  title = models.CharField(max_length=100)
  def __str__(self):
    return self.title

class Project_Category(models.Model):
  title = models.CharField(max_length=100)
  def __str__(self):
    return self.title

class Project_Design(models.Model):
  title = models.CharField(max_length=100)
  def __str__(self):
    return self.title



class Portfolio(models.Model):
  date_published = models.DateField()
  main_project_title = models.CharField(max_length=200)
  description = models.TextField()
  project_hero_image = models.ImageField(upload_to='new_media/')
  project_result = HTMLField()

  filter_category = models.ForeignKey(Project_Category, on_delete=models.CASCADE)
  project_category = models.ManyToManyField(Category)
  project_strategy = models.ManyToManyField(Project_Strategy)
  project_design = models.ManyToManyField(Project_Design)
  project_video_link = models.CharField(max_length = 500)

  project_video_thumbnail = models.ImageField(upload_to='new_media/')
  project_challenge = HTMLField()

  photo_1 = models.ImageField(upload_to='new_media/')
  photo_2 = models.ImageField(upload_to='new_media/')

  selected_work = models.BooleanField()

  user_name = models.CharField(max_length=50)
  user_profile_pic = models.ImageField(upload_to='new_media/',blank=True, null=True)
  user_testimonial = models.TextField()
  user_position = models.CharField(max_length = 70)
  user_company = models.CharField(max_length = 90)

  photo_3 = models.ImageField(upload_to='new_media/')
  company_logo = models.ImageField(upload_to='new_media/',blank=True, null=True)
  new_portfolio_slug = AutoSlugField(populate_from='user_company',unique=True, null=True, default=None )
  def get_absolute_url(self):
    return reverse('portfolio_detail',kwargs={
      'slug':self.new_portfolio_slug
    })

  def __str__(self):
    return self.user_company
