from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
import pytz

ALL_TIMEZONES = sorted((item, item) for item in pytz.all_timezones)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    tz = models.CharField("Timezone", choices=ALL_TIMEZONES,
                          max_length=64, default="('UTC', 'UTC')")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
