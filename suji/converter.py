#:coding=utf-8:
from __future__ import absolute_import

from .accumulator import Acc
from .char import *


def values(src):
    val = []
    acc = Acc()

    for i in range(0, len(src)):
        if is_delimiter(src[i]):
            acc.index_increment(i)
            continue

        if is_decimal_point(src[i]):
            acc.turn_to_decimal_state(i)
            continue

        cardinal = get_cardinal(src[i])
        if cardinal is not None:
            if acc.inside:
                acc.attach_cardinal(i, cardinal)
            elif 1 < cardinal:
                acc.attach_cardinal(i, cardinal)
            continue

        number = get_number(src[i])
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


__all__ = ['values'];
