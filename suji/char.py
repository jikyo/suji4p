""" The mapping and methods from japanese number char to numerical value.
"""


class Char:

    __number = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '０': 0,
        '１': 1,
        '２': 2,
        '３': 3,
        '４': 4,
        '５': 5,
        '６': 6,
        '７': 7,
        '８': 8,
        '９': 9,
        '〇': 0,
        '一': 1,
        '二': 2,
        '三': 3,
        '四': 4,
        '五': 5,
        '六': 6,
        '七': 7,
        '八': 8,
        '九': 9,
        '零': 0,
        '壱': 1,
        '弐': 2,
        '参': 3,
        '肆': 4,
        '伍': 5,
        '陸': 6,
        '漆': 7,
        '捌': 8,
        '玖': 9,
        'Ⅰ': 1,
        'Ⅱ': 2,
        'Ⅲ': 3,
        'Ⅳ': 4,
        'Ⅴ': 5,
        'Ⅵ': 6,
        'Ⅶ': 7,
        'Ⅷ': 8,
        'Ⅸ': 9,
        'Ⅹ': 10,
        'Ⅺ': 11,
        'Ⅻ': 12,
        'ⅰ': 1,
        'ⅱ': 2,
        'ⅲ': 3,
        'ⅳ': 4,
        'ⅴ': 5,
        'ⅵ': 6,
        'ⅶ': 7,
        'ⅷ': 8,
        'ⅸ': 9,
        'ⅹ': 10,
        'ⅺ': 11,
        'ⅻ': 12,
    }

    __cardinal = {
        '十': 10,
        '百': 100,
        '千': 1000,
        '万': 10000,
        '億': 100000000,
        '兆': 1000000000000,
        '京': 10000000000000000,
        '拾': 10,
        '陌': 100,
        '佰': 100,
        '阡': 1000,
        '仟': 1000,
        '萬': 10000,
        '割': 0.1,
        '分': 0.01,
        '厘': 0.001,
        '毛': 0.0001,
        # '/':	None, # TODO: fraction
        # '／':	None, # TODO: fraction
    }

    __decimal_point = {
        '.':	'Full Stop',
        # '．':	'Full-width Full Stop',
    }

    __delimiter = {
        ',':	'Comma',
        # '、':	'Ideographic Comma',
    }

    @staticmethod
    def is_delimiter(c):
        if c in Char.__delimiter:
            return True
        return False

    @staticmethod
    def is_decimal_point(c):
        if c in Char.__decimal_point:
            return True
        return False

    @staticmethod
    def get_number(c):
        return Char.__number.get(c)

    @staticmethod
    def get_cardinal(c):
        return Char.__cardinal.get(c)
