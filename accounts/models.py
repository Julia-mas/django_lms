from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, default='default.png', upload_to='avatars/')

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
