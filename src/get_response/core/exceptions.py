class WrongResponseType(Exception):
    MESSAGE = """Can't automatically detect type of parsing object. 
    You can use the `response_type` to choose type by your self or 
    check your parsing object for syntax mistakes."""
