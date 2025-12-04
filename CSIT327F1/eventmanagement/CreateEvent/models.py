from django.db import models

from User.models import Teacher, Student


# Create your models here.
#Models: Event (Eventid, EventTitle, DateOfEvent, MaxParticipants, RoomID)
# Room (roomid, roomname)

class Room(models.Model):
    roomid = models.IntegerField(primary_key=True)
    roomname = models.CharField(max_length=50)

    def __str__(self):
        return self.roomname

class Event(models.Model):
    eventid = models.IntegerField(primary_key=True)
    roomid = models.ForeignKey(Room, on_delete=models.CASCADE)
    eventtitle = models.CharField(max_length=50)
    dateofevent = models.DateField()
    maxparticipants= models.IntegerField()
    teacher = models.ManyToManyField(Teacher)
    student = models.ManyToManyField(Student, through="AttendEvent")

class AttendEvent(models.Model):
    eventid = models.ForeignKey(Event, on_delete=models.RESTRICT)
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    status = models.BooleanField(default=False)
    dateregistered = models.DateField()


