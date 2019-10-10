from django.db import models

# Create your models here.
class Comments(models.Model):
    comment = models.CharField(max_length = 200)
    topublish = models.BooleanField(default=False)

    def __str__(self):
        return self.comment + ' | ' + str(self.topublish)
