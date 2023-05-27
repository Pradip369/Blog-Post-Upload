from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return str(self.category_name)

class Post(models.Model):
    title = models.CharField(max_length=200)
    disc = models.TextField()
    category = models.ForeignKey(to = Category,on_delete=models.CASCADE,related_name="post_category")