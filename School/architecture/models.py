from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    author = models.CharField(max_length=30)
    name_product = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    max_users = models.IntegerField()
    min_users = models.IntegerField()


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    video_link = models.URLField()


class ListItems(models.Model):
    member = models.CharField(max_length=200)


class ListStudents(models.Model):
    students_list = models.ForeignKey(ListItems, on_delete=models.CASCADE)


class Groups(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    students = models.ForeignKey(ListStudents, on_delete=models.CASCADE)


class UserProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
