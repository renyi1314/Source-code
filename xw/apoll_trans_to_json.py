#!/usr/bin/env python
# coding=utf-8

import json

apollo_config_text = """
max_length = 1
age = 2
"""


def json_format(plain_configs):
    config_lst = plain_configs.split('\n')
    if config_lst:
        config_json = []
        for line in config_lst:
            if not line.startswith('#') and line.strip():
                k, v = line.split('=', 1)
                config_json.append({
                    # "key": k.strip(),
                    # "value": v.strip(),
                    k.strip(): v.strip()
                })

    return json.dumps(config_json)


if __name__ == '__main__':
    json_items = json_format(apollo_config_text)
    print(json_items)
