import logging
import time
from functools import wraps


def continue_when_error(func):
    """contine when error"""

    @wraps(func)
    def fn(*args, **kwargs):
        """docstring for fn"""
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            logging.error(e)

    return fn


def retry_when_error(func):
    """retry when error"""

    @wraps(func)
    def fn(*args, **kwargs):
        """docstring for fn"""
        for k, item in enumerate(range(3)):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if k == 2:
                    logging.exception(e)

    return fn


def retry_when_error_with_params(*out_args, **out_kwargs):
    def retry_when_error_occur(func):
        @wraps(func)
        def fn(*args, **kwargs):
            """docstring for fn"""

            times = int(out_kwargs.get("times", 5))
            delay = int(out_kwargs.get("delay", 0))
            for k, item in enumerate(range(times)):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if k == times - 1:
                        logging.exception(e)
                        feishu_send(repr(e))
                    if delay > 0:
                        time.sleep(delay)

        return fn

    return retry_when_error_occur


def retry_when_error_with_times(times):
    """retry when error with times params"""
    return retry_when_error_with_params(times=times)


def feishu_alert(func):
    @wraps(func)
    def fn(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.exception(e)
            feishu_send(repr(e))

    return fn


@retry_when_error_with_times(10)
def run():
    try:
        raise Exception("run error")
    except Exception as e:
        return 1
