import datetime

import pytz
from tzlocal import get_localzone


def unix_timestamp_to_datetime(unix_timestamp):
    # Convert the Unix timestamp to a datetime object in UTC
    utc_datetime = datetime.datetime.utcfromtimestamp(unix_timestamp)

    # Convert the UTC datetime object to the local time zone
    local_datetime = utc_datetime.replace(tzinfo=pytz.utc).astimezone(get_localzone())

    return local_datetime
