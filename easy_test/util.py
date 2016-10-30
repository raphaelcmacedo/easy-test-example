def contains_option(meta, attribute):
    value = getattr(meta, attribute, None)
    return value is not None


class HttpMethods:
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'