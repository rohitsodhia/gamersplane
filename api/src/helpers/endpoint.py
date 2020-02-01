def require_values(data_obj, fields=[]):
    missing_fields = []
    for key in fields:
        if key not in data_obj:
            missing_fields.append(key)
    return missing_fields
