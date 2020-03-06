from pprint import pformat
"""
This script converts any given Python data to a valid DynamoDB Item type.
"""

DATA_DICT = {
    'string_item': 'value',
    'list_item': ['item1', 'item2'],
    'map_item': {
        'str_item': 'str_val',
        'list_item': ['li1', 'li2'],
        'map_item': {'mk1': 'mk1val', 'mk2': 'mk2val'},
        'bool_item': True
    },
    'bool_item': True,
    'int_item': 9,
    'float_item': 9.13
}


def convert_dict_to_dynamodb_type(raw_data: dict):
    """"""

    converted_dict = {}
    for key, value in raw_data.items():
        converted_value = _data_to_dynamodb_type(value)
        converted_dict[key] = converted_value

    return converted_dict


def _data_to_dynamodb_type(raw: any) -> dict:
    """"""

    print('Converting given data to DynamoDB item...')

    if isinstance(raw, dict):
        return {"M": {key: _data_to_dynamodb_type(value) for key, value in raw.items()}}

    elif isinstance(raw, list):
        return {"L": [_data_to_dynamodb_type(item) for item in raw]}

    elif isinstance(raw, str):
        return {"S": raw}

    elif isinstance(raw, bool):
        return {"BOOL": raw}

    elif isinstance(raw, (int, float)):
        return {"N": str(raw)}

    elif isinstance(raw, bytes):
        return {"B": raw}

    elif raw is None:
        return {"NULL": True}


if __name__ == '__main__':
    converted_dict = convert_dict_to_dynamodb_type(DATA_DICT)

    print('Conversion complete. Item is:')
    print(pformat(converted_dict))