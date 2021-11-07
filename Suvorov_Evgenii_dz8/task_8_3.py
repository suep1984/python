from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'type {func.__name__}: {type(result)}')
        out = []
        for arg in args:
            out.append(f'{func.__name__}({arg}: {type(arg)})')
        for k, v in kwargs.items():
            out.append(f'{func.__name__}({v}: {type(v)})')
        print(', '.join(out))
        return result

    return wrapper


@type_logger
def calc_cube(x, y):
    return x ** y


# пример вызова
a = calc_cube(x=4, y=3)
