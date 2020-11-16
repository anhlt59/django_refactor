import time
from datetime import datetime

from django import template
from django.conf import settings

register = template.Library()


@register.filter()
def times_convert(time_input=None, frm=None):
    """
    {% load times_convert %}
    {{ var | times_convert }}
    """
    if time_input is None:
        return ''
    time_input = datetime.strptime(str(time_input), settings.DATE_FORMAT)
    time_input = time_input.strftime(frm)
    return time_input
