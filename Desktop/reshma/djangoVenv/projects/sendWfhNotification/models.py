from django.db import models
from django.utils import timezone


class notif(models.Model):
    notifOwner = models.ForeignKey('auth.User')
    subject = models.CharField(max_length=200)
    taskList = models.TextField()
    notif_date = models.DateTimeField(
            default=timezone.now)

    def shoot_notif(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.subject