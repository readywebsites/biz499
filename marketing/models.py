from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Home_services(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  image = models.ImageField(upload_to='new_media/')
  def __str__(self):
    return self.title

class Home_logos(models.Model):
  title = models.CharField(max_length=100)
  logo = models.ImageField(upload_to='new_media/')
  logo_grey = models.ImageField(upload_to='new_media/')
  
  def __str__(self):
    return self.title


class Subscription(models.Model):
  email = models.EmailField()
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.email

class Open_posts(models.Model):
  post = models.CharField(max_length=40)
  description = models.TextField ()

  def __str__(self):
    return self.post

class Job_applications(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  contact = models.IntegerField()
  post = models.ForeignKey("Open_posts",on_delete=models.CASCADE)
  # resume = models.FileField(validators=[validate_file_type], upload_to = 'media/resumes' , blank=True)
  # resume = models.FileField(upload_to = 'media/resumes', blank=True)
  resume = models.FileField(null=True, 
                           blank=True, upload_to = 'media/resumes',
                           validators=[FileExtensionValidator( ['pdf'] ) ])
  def __str__(self):
    return self.post.post

class New_Project(models.Model):
  name = models.CharField(max_length=100)
  email_id = models.EmailField()
  company = models.CharField(max_length=100)
  phone_lead = models.CharField(max_length=20,blank=True,null=True)
  budget_min = models.IntegerField()
  budget_max = models.IntegerField()
  proj_details = models.TextField(blank=True,null=True)

  def __str__(self):
    return self.company

class Payment(models.Model):
  order_id= models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=50,null=True, blank=True)
  email_id_pay = models.EmailField()
  phone = models.CharField(max_length=15,null=True, blank=True)
  amount = models.CharField(max_length=100)
  #service = models.CharField()
  proj_details = models.TextField(null=True, blank=True)
  instamojo_response = models.TextField(null=True, blank=True)
  purpose = models.CharField(max_length=500,null=True, blank=True)
  is_paid = models.BooleanField(default=False)
  payment_id = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.email_id_pay

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
    
class Lead(models.Model):
  full_name = models.CharField(max_length=50)
  contact_number = models.CharField(max_length=50)
  message = models.TextField()

  def __str__(self):
    return self.full_name
  
  



   
