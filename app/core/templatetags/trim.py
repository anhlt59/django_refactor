from django import template

register = template.Library()


@register.filter()
def trim(text):
    """
    {% load trim %}
    {{ var | trim }}
    """
    return text.strip() if text else ""
