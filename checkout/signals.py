from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ update order-total on update/add of lineitem """
    print('save-signal received!')
    instance.order_number.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """ update order-total on delete of lineitem """
    print('delete-signal received!')
    instance.order_number.update_total()
