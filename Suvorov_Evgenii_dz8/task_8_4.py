from functools import wraps


def val_checker(val_func=None):
    def _val_checker(func):
        @wraps(func)
        def wrapper(x):
            result = func(x)
            if val_func(x):
                print(result)
            else:
                msg = f'wrong val {x}'
                raise ValueError(msg)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


# пример вызова
a = calc_cube(5)
b = calc_cube(-5)
