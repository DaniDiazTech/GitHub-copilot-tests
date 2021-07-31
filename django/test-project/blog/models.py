from django.db import models

# Create your models here.

class Post(models.Model):
    """Post model

    name: CharField
    body: TextField
    created, updated: DateTimeField
    """

    name = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    """Comment model
    name: CharField
    body: TextField
    created, updated: DateTimeField
    """

    name = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)

class Tag(models.Model):
    """Tag model
    name: CharField
    """

    name = models.CharField(max_length=100)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.name