from django.db import models


class Article(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=30)
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(to=Article, related_name='comments', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='share/images', blank=True, null=True)

    def __str__(self):
        return self.text


# class Image(models.Model):
#     picture = models.ImageField(upload_to='images/')
#
#     def __str__(self):
#         return self.picture
# class Photo(models.Model):
#     image = models.ImageField(upload_to='myapp')
