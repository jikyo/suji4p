""" The entry point to the converter method.

This provides a method to convert from japanese number notation to numerical value.
"""
from suji.accumulator import Acc
from suji.char import Char


def values(src):
    """ Convert from Japanese number notation to numerical value.
    The return value is a list of result objects.
    If the input string has no number notation, `values` returns a empty list.
    The result object has three keys: `val`, `beg`, and `end`:

    :val: the numerical value of the number notation.
    :beg: the start postion of the found number notation at the input string.
    :end: the end postion of the found number notation.

    :param src: a input string.
    :return: a list of the numerical value objects.
    """
    val = []
    acc = Acc()

    for i in range(0, len(src)):
        if Char.is_delimiter(src[i]):
            acc.index_increment(i)
            continue

        if Char.is_decimal_point(src[i]):
            acc.turn_to_decimal_state(i)
            continue

        cardinal = Char.get_cardinal(src[i])
        if cardinal is not None:
            if acc.inside:
                acc.attach_cardinal(i, cardinal)
            elif 1 < cardinal:
                acc.attach_cardinal(i, cardinal)
            continue

        number = Char.get_number(src[i])
        if number is not None:
            acc.attach_number(i, number)
            continue
        
        if not acc.inside:
            continue

        val.append(acc.get_value())
        acc = Acc()

    if acc.inside:
        val.append(acc.get_value())

    return val


__all__ = ['values']
