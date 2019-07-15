import inspect
import unittest

from suji.kansuji import Kansuji, kansujis


class TestKansuji(unittest.TestCase):

    def setUp(self):
        pass

    def test_kannsuuji_string(self):
        self.assertEqual(Kansuji.string(30), '三十')
        self.assertEqual(Kansuji.string(56), '五十六')
        self.assertEqual(Kansuji.string(100, False), '百')
        self.assertEqual(Kansuji.string(100, True), '一百')
        self.assertEqual(Kansuji.string(111, False), '百十一')
        self.assertEqual(Kansuji.string(1004), '一千四')
        self.assertEqual(Kansuji.string(1004, False), '千四')
        self.assertEqual(Kansuji.string(10005), '一万五')
        self.assertEqual(Kansuji.string(10005, False), '万五')
        self.assertEqual(Kansuji.string(20000005), '二千万五')
        self.assertEqual(Kansuji.string(10000000), '一千万')
        self.assertEqual(Kansuji.string(10000000, False), '千万')
        self.assertEqual(Kansuji.string(20010300), '二千一万三百')
        self.assertEqual(Kansuji.string(2000000607), '二十億六百七')
        self.assertEqual(Kansuji.string(32.001), '三十二')

    def test_kannsuuji_minus(self):
        self.assertEqual(Kansuji.string(-20010300), 'マイナス二千一万三百')
        self.assertEqual(Kansuji.string(-0), '零')
        self.assertEqual(Kansuji.string(-1), 'マイナス一')
        self.assertEqual(Kansuji.string(-100000000, True), 'マイナス一億')

    def test_kansuji(self):
        expect = []
        self.assertListEqual(kansujis('文字'), expect)

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
            {'val': '二兆三十万五千十七', 'beg': 0, 'end': 9},
        ]
        self.assertListEqual(kansujis('二兆30万五千十7円になります。', False), expect)
