import inspect
import unittest

from suji.kansuji import Kansuji, kansujis, kansuji


class TestKansuji(unittest.TestCase):

    def setUp(self):
        pass

    def test_empty_0(self):
        self.assertEqual(kansujis(''), [])

    def test_empty_1(self):
        self.assertEqual(kansujis('こんにちは'), [])

    def test_Kansuji_value_000(self):
        self.assertEqual(Kansuji.value(30), '三十')

    def test_Kansuji_value_001(self):
        self.assertEqual(Kansuji.value(56), '五十六')

    def test_Kansuji_value_002(self):
        self.assertEqual(Kansuji.value(100, False), '百')

    def test_Kansuji_value_003(self):
        self.assertEqual(Kansuji.value(100, True), '一百')

    def test_Kansuji_value_004(self):
        self.assertEqual(Kansuji.value(111, False), '百十一')

    def test_Kansuji_value_005(self):
        self.assertEqual(Kansuji.value(1004), '一千四')

    def test_Kansuji_value_006(self):
        self.assertEqual(Kansuji.value(1004, False), '千四')

    def test_Kansuji_value_007(self):
        self.assertEqual(Kansuji.value(10005), '一万五')

    def test_Kansuji_value_008(self):
        self.assertEqual(Kansuji.value(10005, False), '万五')

    def test_Kansuji_value_009(self):
        self.assertEqual(Kansuji.value(20000005), '二千万五')

    def test_Kansuji_value_010(self):
        self.assertEqual(Kansuji.value(10000000), '一千万')

    def test_Kansuji_value_011(self):
        self.assertEqual(Kansuji.value(10000000, False), '千万')

    def test_Kansuji_value_012(self):
        self.assertEqual(Kansuji.value(20010300), '二千一万三百')

    def test_Kansuji_value_013(self):
        self.assertEqual(Kansuji.value(2000000607), '二十億六百七')

    def test_Kansuji_value_014(self):
        self.assertEqual(Kansuji.value(32.001), '三十二')

    def test_Kansuji_value_minus_000(self):
        self.assertEqual(Kansuji.value(-20010300), 'マイナス二千一万三百')

    def test_Kansuji_value_minus_001(self):
        self.assertEqual(Kansuji.value(-0), '零')

    def test_Kansuji_value_minus_002(self):
        self.assertEqual(Kansuji.value(-1), 'マイナス一')

    def test_Kansuji_value_minus_003(self):
        self.assertEqual(Kansuji.value(-100000000, True), 'マイナス一億')

    def test_Kansuji_value_decimal_000(self):
        self.assertEqual(Kansuji.value(-1.1), 'マイナス一')

    def test_Kansuji_value_decimal_001(self):
        self.assertEqual(Kansuji.value(-100.234, False), 'マイナス百')

    def test_kansujis_000(self):
        expect = [
            {'val': '零', 'beg': 0, 'end': 1},
        ]
        self.assertListEqual(kansujis('0'), expect)

    def test_kansujis_001(self):
        expect = [
            {'val': '一', 'beg': 0, 'end': 1},
        ]
        self.assertListEqual(kansujis('1'), expect)

    def test_kansujis_002(self):
        expect = [
            {'val': '十', 'beg': 0, 'end': 2},
        ]
        self.assertListEqual(kansujis('10', False), expect)

    def test_kansujis_003(self):
        expect = [
            {'val': '一十', 'beg': 0, 'end': 2},
        ]
        self.assertListEqual(kansujis('10', True), expect)

    def test_kansujis_004(self):
        expect = [
            {'val': '九十九万九千九百九十九', 'beg': 0, 'end': 6},
        ]
        self.assertListEqual(kansujis('999999'), expect)

    def test_kansujis_005(self):
        expect = [
            {'val': '九十九万九千一百', 'beg': 0, 'end': 6},
        ]
        self.assertListEqual(kansujis('999100'), expect)

    def test_kansujis_006(self):
        expect = [
            {'val': '九十九万九千百', 'beg': 0, 'end': 6},
        ]
        self.assertListEqual(kansujis('999100', False), expect)

    def test_kansujis_007(self):
        expect = [
            {'val': '一千万', 'beg': 0, 'end': 6},
        ]
        self.assertListEqual(kansujis('1,000万'), expect)

    def test_kansujis_008(self):
        expect = [
            {'val': '千万', 'beg': 0, 'end': 6},
        ]
        self.assertListEqual(kansujis('1,000万', False), expect)

    def test_kansujis_009(self):
        expect = [
            {'val': '一千万五十六', 'beg': 4, 'end': 14},
        ]
        self.assertListEqual(kansujis('価格は￥10,000,056です。'), expect)

    def test_kansujis_010(self):
        expect = [
            {'val': '千万五十六', 'beg': 4, 'end': 14},
        ]
        self.assertListEqual(kansujis('価格は￥10,000,056です。', False), expect)

    def test_kansujis_011(self):
        expect = [
            {'val': '一', 'beg': 0, 'end': 1},
            {'val': '二兆三十万五千十七', 'beg': 6, 'end': 15},
        ]
        self.assertEqual(kansujis('１つの価格が二兆30万五千十7円になります。', False), expect)

    def test_kansujis_012(self):
        expect = [
            {'val': '一', 'beg': 0, 'end': 1},
            {'val': '二兆三十万五千一十七', 'beg': 6, 'end': 15},
        ]
        self.assertEqual(kansujis('１つの価格が二兆30万五千十7円になります。'), expect)

    def test_kansuji_000(self):
        self.assertEqual(kansuji('0'), '零')

    def test_kansuji_001(self):
        self.assertEqual(kansuji('それは0'), 'それは零')

    def test_kansuji_002(self):
        self.assertEqual(kansuji('0は零'), '零は零')

    def test_kansuji_003(self):
        self.assertEqual(kansuji('1'), '一')

    def test_kansuji_004(self):
        self.assertEqual(kansuji('10'), '一十')

    def test_kansuji_005(self):
        self.assertEqual(kansuji('10', False), '十')

    def test_kansuji_006(self):
        self.assertEqual(kansuji('11', False), '十一')

    def test_kansuji_007(self):
        self.assertEqual(kansuji('11'), '一十一')

    def test_kansuji_008(self):
        self.assertEqual(kansuji('これは999999です。'), 'これは九十九万九千九百九十九です。')

    def test_kansuji_009(self):
        self.assertEqual(kansuji('これは999100です。'), 'これは九十九万九千一百です。')

    def test_kansuji_010(self):
        self.assertEqual(kansuji('これは999100です。', False), 'これは九十九万九千百です。')

    def test_kansuji_011(self):
        self.assertEqual(kansuji('価格は￥10,000,056です。'), '価格は￥一千万五十六です。')

    def test_kansuji_012(self):
        self.assertEqual(kansuji('価格は￥10,000,056です。', False), '価格は￥千万五十六です。')

    def test_kansuji_013(self):
        self.assertEqual(kansuji('１つの価格が二兆30万五千十7円になります。'), '一つの価格が二兆三十万五千一十七円になります。')

    def test_kansuji_014(self):
        self.assertEqual(kansuji('１つの価格が二兆30万五千十7円になります。', False), '一つの価格が二兆三十万五千十七円になります。')
