from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    class Meta:
        ordering  = ('-created',)


    def __str__(self):
        return f'{self.slug} - {self.updated}' 

    def get_absolute_url(self):
        return reverse('home:post_detail',  args=(self.slug,))


    def like_count(self):
        return self.pvote.count()

    def user_can_like(self , user ):
        user_like = user.uvote.filter(post= self)
        if user_like.exists():
            return True
        return False

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='ucomments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name='pcomments')
    replay = models.ForeignKey('self' , on_delete=models.CASCADE , blank=True , null= True , related_name='rcomments')
    is_replay = models.BooleanField(default=False)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user} - {self.body[:30]}'


class Vote (models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE , related_name='uvote')
    post = models.ForeignKey(Post ,on_delete=models.CASCADE , related_name='pvote')

    def __str__(self) -> str:
        return f'{self.user} liked {self.post.slug}'