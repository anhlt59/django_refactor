from django import template

register = template.Library()


@register.filter()
def unicode_replace(text):
    """
    {% load unicode_replace %}
    {{ var | unicode_replace }}
    """
    text = text.replace('&mdash;', '—')
    text = text.replace('&ndash;', '–')
    text = text.replace('&lsquo;', '‘')
    text = text.replace('&rsquo;', '’')
    text = text.replace('&sbquo;', '‚')
    text = text.replace('&ldquo;', '“')
    text = text.replace('&rdquo;', '”')
    text = text.replace('&bdquo;', '„')
    text = text.replace('&lsaquo;', '‹')
    text = text.replace('&rsaquo;', '›')
    return text
