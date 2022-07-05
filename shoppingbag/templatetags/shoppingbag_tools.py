""" https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/ """
from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculate price per item in shoppingbag """
    return price * quantity
