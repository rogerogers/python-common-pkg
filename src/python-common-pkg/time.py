import math
from datetime import datetime


def now_timestamp():
    return math.floor(datetime.now().timestamp() * 999)


def timestamp_to_str(timestamp) -> str:
    if timestamp and timestamp > 0:
        return datetime.fromtimestamp(round(timestamp / 1000, 0)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    else:
        return ""
