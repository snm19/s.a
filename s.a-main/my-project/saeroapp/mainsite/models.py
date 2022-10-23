from email.policy import default
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField



class Category(models.Model):
    name=models.CharField(max_length=250)   
    slug=models.SlugField(null=True,unique=True,db_index=True,editable=False,blank=True) 
    image=models.ImageField(null=False,upload_to="teamimages")



    def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super().save(*args, **kwargs)    

    def __str__(self):
        return f"{self.name}"








class staff(models.Model):
    name=models.CharField(max_length=50)
    task=models.CharField(max_length=100)
    image=models.ImageField(upload_to="personimages")
    description=RichTextField()
    linkedin_adress=models.TextField(null=True)
    is_active=models.BooleanField(default=False)
    slug=models.SlugField(null=False,blank=True,unique=True,db_index=True)
    categories=models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.task}"

    def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super().save(*args, **kwargs)    



class Sponsors(models.Model):
    name=models.CharField(max_length=250)
    describtion=models.CharField(max_length=250)
    image=models.ImageField(upload_to="sponsorimages")
    slug=models.SlugField(null=True,unique=True,db_index=True,editable=False,blank=True)


    def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super().save(*args, **kwargs)    

    def __str__(self):
        return f"{self.name}"


class Carousel(models.Model):
    title=models.CharField(max_length=250)
    describtion=models.CharField(max_length=400)
    image=models.ImageField(upload_to="carouselimages")


    def save(self, *args, **kwargs):
      self.slug = slugify(self.title)
      super().save(*args, **kwargs)    

    def __str__(self):
        return f"{self.title}"        




    
