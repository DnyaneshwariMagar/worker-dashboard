from django.db import models

# Create your models here.

class Worker(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Workstation(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Event(models.Model):
    timestamp = models.DateTimeField()
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    workstation = models.ForeignKey(Workstation, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    confidence = models.FloatField()
    count = models.IntegerField(null=True, blank=True)

    def __str__(self):
       return f"{self.worker.name} - {self.event_type} - {self.timestamp}"