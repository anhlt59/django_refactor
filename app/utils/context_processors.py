from django.conf import settings


def settings_context(_request):
    """
    Settings available by default to the templates context.
    /config/settings/base.py
    TEMPLATES[0]["OPTIONS"]["context_processors"] = app.utils.context_processors.settings_context
    """
    return {
        "DEBUG": settings.DEBUG,
        "YEAR": settings.CONSTANTS.common.YEAR,
    }
