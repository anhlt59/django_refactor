import pytz
import datetime
from django.conf import settings

TIME_ZONE = pytz.timezone(settings.TIME_ZONE)
DATETIME_FORMAT = settings.DATETIME_INPUT_FORMATS[0]
TIME_FORMAT = settings.TIME_INPUT_FORMATS[0]
DATE_FORMAT = settings.DATE_INPUT_FORMATS[0]


def get_current_time():
    return datetime.datetime.now(TIME_ZONE)


def get_current_date():
    return get_current_time().date()


def format_datetime(dt):
    assert dt.tzinfo, "Timezone is required"

    if type(dt) is datetime.datetime:
        format = DATETIME_FORMAT
    elif type(dt) is datetime.date:
        format = DATE_FORMAT
    elif type(dt) is datetime.time:
        format = TIME_FORMAT
    else:
        raise ValueError("Type error")
    return dt.strftime(format)


def get_school_year():
    today = get_current_date()
    return today.year + 1 if today.month < 4 else today.year + 2
