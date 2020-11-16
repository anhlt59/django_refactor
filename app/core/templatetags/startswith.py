from django import template

register = template.Library()


@register.filter('startswith')
def startswith(text, starts):
    """
     {% load startswith %}

    {{ var | startswith: "foo" }}
    """
    return text.startswith(starts) if isinstance(text, str) else False
