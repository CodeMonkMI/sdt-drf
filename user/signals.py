from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from user.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()


@receiver(post_save, sender=User)
def assign_default_role(sender, instance, created, **kwargs):
    if created:
        user_group, created = Group.objects.get_or_create(name="member")
        instance.groups.add(user_group)
        instance.save()
