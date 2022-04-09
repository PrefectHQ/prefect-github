import json
import re
from collections import defaultdict

SNAKE_CASE1 = re.compile("(.)([A-Z][a-z]+)")
SNAKE_CASE2 = re.compile("([a-z0-9])([A-Z])")


def _to_snake_case(name):
    name = SNAKE_CASE1.sub(r"\1_\2", name)
    return SNAKE_CASE2.sub(r"\1_\2", name).lower()


def initialize_return_fields_defaults(config_path):
    with open(config_path, "r") as f:
        config = json.load(f)

    return_fields_defaults = defaultdict(lambda: [])
    for op_type, sub_op_types in config.items():
        for sub_op_type in sub_op_types:
            if isinstance(sub_op_type, str):
                return_fields_defaults[(op_type,)].append(_to_snake_case(sub_op_type))
            elif isinstance(sub_op_type, dict):
                sub_op_type_key = list(sub_op_type.keys())[0]
                return_fields_defaults[(op_type, sub_op_type_key)] = [
                    _to_snake_case(field) for field in sub_op_type[sub_op_type_key]
                ]
    return return_fields_defaults
