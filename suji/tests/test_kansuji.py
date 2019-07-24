import inspect
import unittest

from suji.kansuji import Kansuji, kansujis, kansuji


class TestKansuji(unittest.TestCase):

    def setUp(self):
        pass

    def test_empty(self):
        self.assertEqual(kansujis(''), [])
        self.assertEqual(kansujis('こんにちは'), [])

    def test_Kansuji_value(self):
        self.assertEqual(Kansuji.value(30), '三十')
        self.assertEqual(Kansuji.value(56), '五十六')
        self.assertEqual(Kansuji.value(100, False), '百')
        self.assertEqual(Kansuji.value(100, True), '一百')
        self.assertEqual(Kansuji.value(111, False), '百十一')
        self.assertEqual(Kansuji.value(1004), '一千四')
        self.assertEqual(Kansuji.value(1004, False), '千四')
        self.assertEqual(Kansuji.value(10005), '一万五')
        self.assertEqual(Kansuji.value(10005, False), '万五')
        self.assertEqual(Kansuji.value(20000005), '二千万五')
        self.assertEqual(Kansuji.value(10000000), '一千万')
        self.assertEqual(Kansuji.value(10000000, False), '千万')
        self.assertEqual(Kansuji.value(20010300), '二千一万三百')
        self.assertEqual(Kansuji.value(2000000607), '二十億六百七')
        self.assertEqual(Kansuji.value(32.001), '三十二')

    def test_Kansuji_value_minus(self):
        self.assertEqual(Kansuji.value(-20010300), 'マイナス二千一万三百')
        self.assertEqual(Kansuji.value(-0), '零')
        self.assertEqual(Kansuji.value(-1), 'マイナス一')
        self.assertEqual(Kansuji.value(-100000000, True), 'マイナス一億')

    def test_Kansuji_value_decimal(self):
        self.assertEqual(Kansuji.value(-1.1), 'マイナス一')
        self.assertEqual(Kansuji.value(-100.234, False), 'マイナス百')

    def test_kansujis(self):
        expect = [
            {'val': '零', 'beg': 0, 'end': 1},
        ]
        self.assertListEqual(kansujis('0'), expect)

        expect = [
            {'val': '一', 'beg': 0, 'end': 1},
        ]
        self.assertListEqual(kansujis('1'), expect)

        expect = [
            {'val': '十', 'beg': 0, 'end': 2},
        ]
        self.assertListEqual(kansujis('10', False), expect)

        expect = [
            {'val': '一十', 'beg': 0, 'end': 2},
        ]
        self.assertListEqual(kansujis('10', True), expect)

        expect = [
            {'val': '九十九万九千九百九十九', 'beg': 0, 'end': 6},
        ]
        self.assertListEqual(kansujis('999999'), expect)

        expect = [
            {'val': '九十九万九千一百', 'beg': 0, 'end': 6},
        ]
        self.assertListEqual(kansujis('999100'), expect)

        expect = [
            {'val': '九十九万九千百', 'beg': 0, 'end': 6},
        ]
        self.assertListEqual(kansujis('999100', False), expect)

        expect = [
            {'val': '一千万', 'beg': 0, 'end': 6},
        ]
        self.assertListEqual(kansujis('1,000万'), expect)

        expect = [
            {'val': '千万', 'beg': 0, 'end': 6},
        ]
        self.assertListEqual(kansujis('1,000万', False), expect)

        expect = [
            {'val': '一千万五十六', 'beg': 4, 'end': 14},
        ]
        self.assertListEqual(kansujis('価格は￥10,000,056です。'), expect)

        expect = [
            {'val': '千万五十六', 'beg': 4, 'end': 14},
        ]
        self.assertListEqual(kansujis('価格は￥10,000,056です。', False), expect)

        expect = [
            {'val': '一', 'beg': 0, 'end': 1},
            {'val': '二兆三十万五千十七', 'beg': 6, 'end': 15},
        ]
        self.assertEqual(kansujis('１つの価格が二兆30万五千十7円になります。', False), expect)

        expect = [
            {'val': '一', 'beg': 0, 'end': 1},
            {'val': '二兆三十万五千一十七', 'beg': 6, 'end': 15},
        ]
        self.assertEqual(kansujis('１つの価格が二兆30万五千十7円になります。'), expect)

    def test_kansuji(self):
        self.assertEqual(kansuji('0'), '零')
        self.assertEqual(kansuji('それは0'), 'それは零')
        self.assertEqual(kansuji('0は零'), '零は零')
        self.assertEqual(kansuji('1'), '一')
        self.assertEqual(kansuji('10'), '一十')
        self.assertEqual(kansuji('10', False), '十')
        self.assertEqual(kansuji('11', False), '十一')
        self.assertEqual(kansuji('11'), '一十一')
        self.assertEqual(kansuji('これは999999です。'), 'これは九十九万九千九百九十九です。')
        self.assertEqual(kansuji('これは999100です。'), 'これは九十九万九千一百です。')
        self.assertEqual(kansuji('これは999100です。', False), 'これは九十九万九千百です。')
        self.assertEqual(kansuji('価格は￥10,000,056です。'), '価格は￥一千万五十六です。')
        self.assertEqual(kansuji('価格は￥10,000,056です。', False), '価格は￥千万五十六です。')
        self.assertEqual(kansuji('１つの価格が二兆30万五千十7円になります。'), '一つの価格が二兆三十万五千一十七円になります。')
        self.assertEqual(kansuji('１つの価格が二兆30万五千十7円になります。', False), '一つの価格が二兆三十万五千十七円になります。')
