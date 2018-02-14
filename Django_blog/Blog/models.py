from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=20)

    author = models.ForeignKey(User)

    body = models.TextField()

    #image = models.ImageField(upload_to = 'pic_folder/')

    cat = models.ForeignKey(Category)

    likes = models.IntegerField()

    dislikes = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





class Comment(models.Model):

    user = models.ForeignKey(User)

    post = models.ForeignKey(Post)

    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)




class Category_Subscribe(models.Model):

    user = models.ForeignKey(User)

    cat = models.ForeignKey(Category)

    status = models.IntegerField()




class BadWord(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post_Tag(models.Model):

    tag = models.ForeignKey(Tag)

    post = models.ForeignKey(Post)


class Reply(models.Model):
    user = models.ForeignKey(User)

    comment = models.ForeignKey(Comment)

    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)









