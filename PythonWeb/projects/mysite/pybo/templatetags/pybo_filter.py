# ---------------------------------------- [edit] ---------------------------------------- #
from django import template

register = template.Library()

# when creating filter function, @register.filter annotation should be applied.
@register.filter
def sub(value, arg):
    return value - arg
# ---------------------------------------------------------------------------------------- #