from django import template
register = template.Library()

@register.filter
def cutout(value, arg):
    """
    This custs out all values of arg from the string.
    """
    return value.replace(arg, '')
