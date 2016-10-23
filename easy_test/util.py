def contains_option(meta, attribute):
    value = getattr(meta, attribute, None)
    return value is not None
