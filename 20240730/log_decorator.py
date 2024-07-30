import logging


def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        logging.info(f"Function '{func.__name__}' has been called with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' has finished with result: {result}")
        return result
    return wrapper


@log_decorator
def log_function(a, b, c =3):
    return a + b + c



log_function(1, 2)