

def numeric_range(iterable):
    """Find the difference between highest and lowest elements

    Keyword arguments:
    iterable -- an iterable of numeric values
    """

    iterable = list(iterable)

    if len(iterable) == 0:
        return 0

    diff = 0
    low = iterable[0]
    high = iterable[0]
    
    for value in iterable:
        if value < low:
            low = value
        if value >= high:
            high = value

    diff = high - low

    return diff

    
