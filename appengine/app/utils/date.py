#!/usr/bin/env python
import datetime, re, time

from pytz.gae import pytz


################################################################
#
#  Date Utils
#
################################################################
def to_epoch(d):
    return int(time.mktime(d.timetuple()) * 1000)

def text_date(s):
    return s.strftime("%b %d, %Y")

def text_time(dt, local_timezone='EST'):
    TZ_LOCAL = pytz.timezone(local_timezone)
    TZ_GMT = pytz.timezone('GMT')
    local_dt = TZ_GMT.localize(dt).astimezone(TZ_LOCAL)
    str_date = local_dt.strftime("%I:%M %p")
    return "%s (%s)" % (str_date,local_timezone)

def time_delta(td):
    return float((td.seconds*1000000) + td.microseconds) / 1000000

def pretty_date(time=False):
    from datetime import datetime
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 60:
            return "Less than a minute ago"
        if second_diff < 120:
            return  "One minute ago"
        if second_diff < 3600:
            return str( second_diff / 60 ) + " minutes ago"
        if second_diff < 7200:
            return "An hour ago"
        if second_diff < 86400:
            return str( second_diff / 3600 ) + " hours ago"

    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 14:
        return "1 week ago"
    if day_diff < 31:
        return str(day_diff/7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff/30) + " months ago"
    return str(day_diff/365) + " years ago"

