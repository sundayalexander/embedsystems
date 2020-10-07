__author__ = 'Edward'

import os
from datetime import date, datetime, timedelta

import pytz
from django import template
from django.template import defaultfilters
from django.utils.timesince import timesince
from django.utils.timezone import get_current_timezone
from django.utils.translation import ugettext as _, ungettext

tz = pytz.timezone('Africa/Lagos')

register = template.Library()


@register.filter
def natural_time(value):
    """
    Returns a 'natural' representation of the given time.
    Formats similar to Facebook.
    Based on django.contrib.humanize.naturaltime

    If given time occurred today, prints 'x seconds/minutes/hours ago'
    If given time occurred yesterday, prints 'yesterday at xx:xx'
    If given time occurred more than 1 day ago, prints full date
    """
    if not isinstance(value, date):  # datetime is a subclass of date
        return value

    current_timezone = get_current_timezone()
    now = datetime.now(current_timezone)
    yesterday = now - timedelta(days=1)
    value = value.astimezone(current_timezone)  # localize timezone

    delta = now - value
    if value.date() == yesterday.date():
        return _('yesterday at %(time)s') % {'time': defaultfilters.time(value, 'TIME_FORMAT')}
    elif delta.days != 0:
        return defaultfilters.date(value, 'DATETIME_FORMAT')
    elif delta.seconds == 0:
        return _('now')
    elif delta.seconds < 60:
        return ungettext(
            # Translators: please keep a non-breaking space (U+00A0)
            # between count and time unit.
            'a second ago', '%(count)s seconds ago', delta.seconds
        ) % {'count': delta.seconds}
    elif delta.seconds // 60 < 60:
        count = delta.seconds // 60
        return ungettext(
            # Translators: please keep a non-breaking space (U+00A0)
            # between count and time unit.
            'a minute ago', '%(count)s minutes ago', count
        ) % {'count': count}
    else:
        count = delta.seconds // 60 // 60
        return ungettext(
            # Translators: please keep a non-breaking space (U+00A0)
            # between count and time unit.
            'an hour ago', '%(count)s hours ago', count
        ) % {'count': count}


@register.filter(name='range')
def loop_times(number):
    return range(number)


@register.filter(name='times')
def times(query_set, number):
    return query_set[:number]


@register.filter(name='this_field')
def this_field(value):
    # print(value.field.__class__.__name__)
    return value.field.__class__.__name__


@register.filter
def cool_number(value, num_decimals=2):
    """
    Django template filter to convert regular numbers to a
    cool format (ie: 2K, 434.4K, 33M...)
    :param value: number
    :param num_decimals: Number of decimal digits
    """

    int_value = int(value)
    formatted_number = '{{:.{}f}}'.format(num_decimals)
    if int_value < 1000:
        return str(int_value)
    elif int_value < 1000000:
        return formatted_number.format(int_value / 1000.0).rstrip('0.') + 'K'
    else:
        return formatted_number.format(int_value / 1000000.0).rstrip('0.') + 'M'


@register.filter
def split(value, splitter="\r\n"):
    if splitter == "\r\n":
        print(splitter)
        if value.find('\r\n') != -1:
            return value.split('\r\n')
        return value.split('\r\n\r\n')
    return value.split(splitter)


@register.filter
def calc_discount(value, discount):
    discounted = value * (discount/100)
    return value-discounted


@register.filter
def datetime_expired(value):
    if datetime.now().astimezone(tz) > value.astimezone(tz):
        return "Expired"
    else:
        return timesince(value)


datetime_expired.is_safe = False


@register.filter
def partition(thelist, n):
    """
    Break a list into ``n`` pieces. The last list may be larger than the rest if
    the list doesn't break cleanly. That is::

        >>> l = range(10)

        >>> partition(l, 2)
        [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]

        >>> partition(l, 3)
        [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9]]

        >>> partition(l, 4)
        [[0, 1], [2, 3], [4, 5], [6, 7, 8, 9]]

        >>> partition(l, 5)
        [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]

    """
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    p = len(thelist) / n
    return [thelist[p * i:p * (i + 1)] for i in range(n - 1)] + [thelist[p * (i + 1):]]


@register.filter
def partition_horizontal(thelist, n):
    """
    Break a list into ``n`` peices, but "horizontally." That is,
    ``partition_horizontal(range(10), 3)`` gives::

        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10]]

    Clear as mud?
    """
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]

    if len(thelist) <= n:
        n = 1
    else:
        if len(thelist) % n > 0:
            n += 1
        else:
            n = int(len(thelist) / n)

    newlists = [list() for i in range(n)]

    for i, val in enumerate(thelist):
        newlists[i // n].append(val)

    final_list = [listt for listt in newlists if len(listt) > 0]
    return final_list


@register.filter
def wait_time(date_time, mins):
    eta = date_time + timedelta(minutes=mins)
    if eta < datetime.now(tz):
        eta = "Due"

    return eta


@register.filter
def get_extension(name):
    if name:
        name, extension = os.path.splitext(name)
        return extension.replace('.', '')
    return ''
