__author__ = 'Edward'


from django.db.models.signals import post_save, m2m_changed, pre_save
from django.dispatch import receiver

from .enums import UserTypes
from .models import User, UserSetting, OTP


@receiver(post_save, sender=User)
def create_user_addons(sender, instance, created, *args, **kwargs):
    if created:
        UserSetting(user=instance).save()
        OTP(user=instance).save()
    else:
        if hasattr(instance, 'usersetting'):
            instance.usersetting.save()
        if hasattr(instance, 'otp'):
            instance.otp.save()