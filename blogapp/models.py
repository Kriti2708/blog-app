from django.db import models
from django.contrib.auth.models import User


class BlogTimeStamp(models.Model):
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)

   class Meta:
      abstract = True


class Category(BlogTimeStamp):
   name = models.CharField(max_length=100)

   def __str__(self):
      return f"{self.name}"


class Post(BlogTimeStamp):
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   title = models.CharField(max_length=100)
   content = models.TextField(max_length=2000, null=True, blank=True)
   slug = models.SlugField(max_length=1000, null=True, blank=True)
   image = models.ImageField(upload_to='images/', null=True, blank=True)
   posted_on = models.DateTimeField(auto_now=True)
   category = models.ManyToManyField(Category)

   def __str__(self):
      return f'{self.title}'


class Comment(BlogTimeStamp):
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   body = models.TextField(max_length=100)
   posted_on = models.DateTimeField(auto_now=True)

   def __str__(self):
      return f'{self.user}'


class Profile(BlogTimeStamp):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   contact = models.IntegerField(null=True, blank=True)
   picture = models.ImageField(upload_to='images/')
   bio = models.TextField(null=True, blank=True)
