from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    email_id = models.EmailField()
    contact = models.IntegerField()
    balance = models.IntegerField("Balance (₹)")

    def __str__(self):
        return self.username

class Action(models.Model):
    username = models.CharField(max_length=30)
    email_id = models.EmailField()
    contact = models.IntegerField()
    amount = models.IntegerField("Amount (₹)")

    def __str__(self):
        return self.username

class Transact(models.Model):
    username = models.CharField(max_length=30)
    email_id = models.EmailField()
    contact = models.IntegerField()
    amount = models.IntegerField("Amount (₹)")
    receiver = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class History(models.Model):
    username = models.CharField(max_length=30)
    email_id = models.EmailField()
    contact = models.IntegerField()
    amount = models.IntegerField("Amount (₹)")
    action = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.username