from typing import Any


def strip_empty_dicts(dict_in: dict[Any, Any]) -> dict[Any, Any]:
    dict_out = {}

    for key, value in dict_in.items():
        if isinstance(value, dict):
            value = strip_empty_dicts(value)
            if len(value) == 0:
                continue

        dict_out[key] = value

    return dict_out
