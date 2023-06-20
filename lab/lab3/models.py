from django.contrib.auth.models import User
from django.db import models


class BlogUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=90)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_change = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField()
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)  # za koj post
    user = models.ForeignKey(to=BlogUser, on_delete=models.CASCADE)  # od koj korisnik

    def __str__(self):
        return self.content


class File(models.Model):
    file = models.FileField(upload_to="files/", null=True, blank=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name


class Block(models.Model):
    blocker = models.ForeignKey(to=BlogUser, on_delete=models.CASCADE, related_name="user_blocker")
    blocked = models.ForeignKey(to=BlogUser, on_delete=models.CASCADE, related_name="user_blocked")

    def __str__(self):
        return str(self.blocker) + " blocked " + str(self.blocked)
