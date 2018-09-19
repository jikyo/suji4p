#:coding=utf-8:
from __future__ import absolute_import

from .accumulator import Acc
from .char import *


def values(src):
    val = []
    acc = Acc()

    for s in src:
        if is_delimiter(s):
            continue

        if acc.inside and is_decimal_point(s):
            acc.turn_to_decimal_state()
            continue

        cardinal = get_cardinal(s)
        if cardinal is not None:
            acc.attach_cardinal(cardinal)
            continue

        number = get_number(s)
        if number is not None:
            acc.attach_number(number)
            continue
        
        if not acc.inside:
            continue

        val.append(acc.get_value())
        acc = Acc()

    if acc.inside:
        val.append(acc.get_value())

    return val


__all__ = ['values'];
