from functools import wraps
from typing import Any, Callable, get_type_hints


def type_check(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):

        hints = get_type_hints(func)
        all_args = dict(zip(func.__code__.co_varnames, args))
        all_args.update(kwargs)

        for arg_name, arg_value in all_args.items():
            if arg_name in hints and not isinstance(arg_value, hints[arg_name]):
                raise TypeError(
                    f"Argument '{arg_name}' must be of type {hints[arg_name]}, got {type(arg_value)} instead.")

        result = func(*args, **kwargs)

        if 'return' in hints and not isinstance(result, hints['return']):
            raise TypeError(f"Return value must be of type {hints['return']}, got {type(result)} instead.")

        return result

    return wrapper


@type_check
def format_data(name: str, age: int, data: dict, other_info=None) -> str:
    other_info_str = ', Other Info : ' + str(other_info) if other_info else ''
    return f"Name: {name}, Age: {age}, Data: {data['key']}{other_info_str}"