def parse_cookie_str(cookie_str):
    cookie_str = cookie_str.strip()
    cookie_dict = {}
    for cookie_kv in cookie_str.split(";"):
        cookie_kv = cookie_kv.strip()
        if cookie_kv.strip() != "":
            kv = split_two(cookie_kv, "=")
            cookie_dict[kv[0].strip()] = kv[1].strip()
    return cookie_dict


def split_two(strings, sep):
    return strings.split(sep, 1)


def parse_header_str(header_str):
    """
    parse a header str to dict
    """
    header_dict = {}
    for header_kv in header_str.split("\n"):
        header_kv = header_kv.strip()
        if header_kv.strip() != "":
            kv = split_two(header_kv, ":")
            header_dict[kv[0].strip()] = kv[1].strip()
    return header_dict
