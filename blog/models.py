from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default="NULL",upload_to='posts_img')
    polls = models.BigIntegerField(default=0)
    likes = models.ManyToManyField(User,blank = True,related_name="post_likes")




    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    def abc(self):
    	return reverse('blog-home')

class Cmts(models.Model):
    comment=models.CharField(max_length=100,blank=True)
    post_title=models.ForeignKey(Post,on_delete=models.CASCADE)
    
    def get_absolute_url(self):
         return reverse('blog-home')

	



    