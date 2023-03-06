import math
import re


def str_to_int(x) -> int:
    x = x.replace(",", "")
    x = x.replace("+", "")
    if type(x) == float or type(x) == int:
        return math.floor(x)
    if "K" in x:
        return math.floor(float(x.replace("K", "")) * 1000)
    if "M" in x:
        return math.floor(float(x.replace("M", "")) * 1000000)
    if "B" in x:
        return math.floor(float(x.replace("B", "")) * 1000 * 1000 * 1000)
    try:
        return int(x)
    except Exception as e:
        return 0


def trim(text):
    if text is None:
        return None
    return re.sub("\n+", "\n", re.sub(r"\s+", " ", text.strip()))
