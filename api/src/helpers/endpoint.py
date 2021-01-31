def require_values(data_obj: object, fields: list) -> list:
    missing_fields = []
    for key in fields:
        if key not in data_obj or not data_obj[key]:
            missing_fields.append(key)
    return missing_fields
