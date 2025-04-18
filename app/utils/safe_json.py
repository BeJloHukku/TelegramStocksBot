import json


def safe_json_parse(data, default=None):
    if data is None:
        return default
    try:
        parsed = json.loads(data) if isinstance(data, str) else data
        return parsed if isinstance(parsed, list) else default
    except (json.JSONDecodeError, TypeError):
        return default