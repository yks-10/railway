from django.db import models

class Ticket(models.Model):
    starting=models.CharField(max_length=40)
    ending=models.CharField(max_length=40)
    date=models.DateField()

    def __str__(self):
        return self.starting



class Train(models.Model):
    train_name=models.CharField(max_length=20)
    train_number=models.IntegerField()
    train_starting=models.CharField(max_length=40)
    train_ending=models.CharField(max_length=40)

    def __str__(self):
        return self.train_name



