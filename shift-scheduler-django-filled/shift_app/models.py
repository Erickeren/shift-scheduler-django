from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ShiftSchedule(models.Model):
    SHIFT_CHOICES = (
        ('Pagi', 'Pagi (08:00 - 20:00)'),
        ('Malam', 'Malam (20:00 - 08:00)'),
    )
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES)

class DayOff(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()
