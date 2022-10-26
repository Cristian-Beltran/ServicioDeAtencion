from django.db import models


def user_directory_path(instance, filename):
    return 'foot/{0}/{1}'.format(instance.name, filename)


class Foot(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=False)
    price = models.FloatField(null=False)
    picture = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return self.name
