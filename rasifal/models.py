from django.db import models
from django.utils import timezone
# Create your models here.


class Rasifal(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.title)


class Rasifal_Desc(models.Model):
    rasi = models.ForeignKey(Rasifal, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = timezone.now().date()
        return super(Rasifal_Desc, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.rasi.title)

    class Meta:
        ordering = ['-date']