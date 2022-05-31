from django.db import models


# Create your models here.
def upload_path(instance, filename):
    return '/'.join(['isse', str(instance.title), filename])


class Images(models.Model):
    title = models.CharField(max_length=50)
    batch_num = models.IntegerField()
    image = models.ImageField(upload_to=upload_path)


