import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# when creating filter function, @register.filter annotation should be applied.
@register.filter
def sub(value, arg):
    return value - arg

# convert input markdown string into html string
@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"] #nl2br : linefeed into <br> tag, fenced_code: markdown into html
                                          # for more: ref: https://python-markdown.github.io/extensions/
    return mark_safe(markdown.markdown(value, extensions=extensions))