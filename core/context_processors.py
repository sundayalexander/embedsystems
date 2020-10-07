__author__ = 'Edward'

from datetime import datetime

import pytz
from django.contrib.sites.models import Site

from core.models import Project

tz = pytz.timezone('Africa/Lagos')


def default(request):
    now = datetime.now(tz)
    if 0 < now.hour <= 12:
        time_of_day = "morning"
    elif 12 < now.hour <= 17:
        time_of_day = "afternoon"
    else:
        time_of_day = "evening"

    try:
        Site.objects.clear_cache()
        site = Site.objects.get_current()
    except:
        site = None

    default_context = {
        'site': site,
        'time_of_day': time_of_day,
        'naira': '₦',
        'recent_projects': Project.objects.all()[:5]
    }

    if request.user.is_authenticated:
        pass
    else:
        pass

    return default_context
