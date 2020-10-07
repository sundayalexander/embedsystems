__author__ = 'Edward'

import json

import pytz
import requests
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.utils.crypto import get_random_string

tz = pytz.timezone('Africa/Lagos')


def format_phone_number(number):
    if len(number) == 13:
        if number.startswith('234'):
            return number
    elif len(number) == 11:
        if number.startswith('0'):
            return number.replace('0', '234', 1)
    elif len(number) == 10:
        return '234' + number
    return None


def unique_generator(model=None, field=None, length=12, allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                                                      'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    if model and field:
        unique = get_random_string(length=length, allowed_chars=allowed_chars)
        kwargs = {field: unique}
        qs_exists = model.objects.filter(**kwargs).exists()
        if qs_exists:
            return unique_generator(model, field)
    else:
        unique = get_random_string(length=length, allowed_chars=allowed_chars)
    return unique


def send_websocket_message(group_name, message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_name,
        message
    )


def call_api(method, url, headers={}, payload={}):
    if method == "get":
        r = requests.get(url, headers=headers, params=payload)
    elif method == "post":
        r = requests.post(url, headers=headers, data=json.dumps(payload))
    elif method == "put":
        r = requests.put(url, headers=headers, data=json.dumps(payload))

    if r.status_code in [200, 201, 204]:
        return r
    else:
        return None
