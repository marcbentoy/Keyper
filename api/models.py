from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    school_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.lastName + ', ' + self.firstName
    

class Building(models.Model):
    name = models.CharField(max_length=100)
    abrv = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    storey = models.IntegerField()
    roomBuilding = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.number


class Key(models.Model):
    rfid = models.CharField(max_length=10, unique=True)
    keyRoom = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.keyRoom.__str__ + '[' + self.rfid + ']'
