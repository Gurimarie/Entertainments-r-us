from django.db import models
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """ 
    user-profile to maintain order-history and delivery-info 
    Can this work for both artists and customers? 
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True,
                                            blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True,
                                   blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwarg):
    """ create or update user-profile """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
    # if existing user, just save profile
