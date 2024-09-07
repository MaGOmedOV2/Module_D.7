from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post (models.Model):

    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(to='Category',on_delete=models.CASCADE,related_name='news')
    author = models.ForeignKey(to= 'Author', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title.title()}: {self.time_in}({self.content})'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Category(models.Model):

    category_name = models.CharField(max_length=50, unique = True)

    def __str__(self):
        return self.category_name.title()


class Author(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)

