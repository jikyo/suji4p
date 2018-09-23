#:coding=utf-8:
import inspect
import unittest

from .. import converter


class TestConverter(unittest.TestCase):

    def setUp(self):
        pass

    def assertFloatArray(self, actual, expected):
        frame = inspect.currentframe().f_back
        m = frame.f_code.co_name 
        m += ' at line ' + str(frame.f_lineno)
        m += '\n' + str(actual) + ' != ' + str(expected)
        self.assertEqual(len(actual), len(expected), msg=m)
        for i in range(0, len(actual)):
            self.assertAlmostEqual(actual[i]['val'], expected[i]['val'], msg=m)
            self.assertAlmostEqual(actual[i]['beg'], expected[i]['beg'], msg=m)
            self.assertAlmostEqual(actual[i]['end'], expected[i]['end'], msg=m)

    def test_values_int(self):
        self.assertEqual(converter.values('こんにちは'), [])

        expect = [
            {'val': 5, 'beg': 0, 'end': 1}
        ]
        self.assertEqual(converter.values('５'), expect)

        expect = [
            {'val': 5, 'beg': 3, 'end': 4}
        ]
        self.assertEqual(converter.values('これは5円です。'), expect)

        expect = [
            {'val': 1000, 'beg': 3, 'end': 8}
        ]
        self.assertEqual(converter.values('これは1,000円です。'), expect)

        expect = [
            {'val': 2, 'beg': 2, 'end': 3}
        ]
        self.assertEqual(converter.values('値は2'), expect)

        expect = [
            {'val': 3000, 'beg': 2, 'end': 7}
        ]
        self.assertEqual(converter.values('値は3,000'), expect)

        expect = [
            {'val': 400, 'beg': 0, 'end': 4}
        ]
        self.assertEqual(converter.values('400, 円になります。'), expect)

        expect = [
            {'val': 1000, 'beg': 0, 'end': 6},
            {'val': 2000, 'beg': 7, 'end': 13},
            {'val': 3000, 'beg': 14, 'end': 20},
        ]
        self.assertEqual(converter.values('1,000, 2,000, 3,000,'), expect)

        expect = [
            {'val': 5, 'beg': 3, 'end': 4},
            {'val': 60, 'beg': 5, 'end': 7},
            {'val': 700, 'beg': 8, 'end': 11},
        ]
        self.assertEqual(converter.values('数列、5、60、700、'), expect)

    def test_values_deciaml(self):
        expect = [
            {'val': 0.6, 'beg': 0, 'end': 3},
        ]
        self.assertFloatArray(converter.values('0.6'), expect)

        expect = [
            {'val': 0.0007, 'beg': 0, 'end': 6},
        ]
        self.assertFloatArray(converter.values('0.0007'), expect)

        expect = [
            {'val': 0.987654321, 'beg': 0, 'end': 11},
        ]
        self.assertFloatArray(converter.values('0.987654321'), expect)

        expect = [
            {'val': 1.3, 'beg': 0, 'end': 3},
        ]
        self.assertFloatArray(converter.values('1.3'), expect)

        expect = [
            {'val': 123.45, 'beg': 0, 'end': 6},
        ]
        self.assertFloatArray(converter.values('123.45'), expect)

        expect = [
            {'val': 1, 'beg': 0, 'end': 2},
        ]
        self.assertFloatArray(converter.values('1.'), expect)

        expect = [
            {'val': 1, 'beg': 3, 'end': 5},
        ]
        self.assertFloatArray(converter.values('これは1.です。'), expect)

        expect = [
            {'val': 0.325, 'beg': 0, 'end': 6},
        ]
        self.assertFloatArray(converter.values('三割二分五厘'), expect)

        expect = [
            {'val': 2.3, 'beg': 0, 'end': 3},
            {'val': 0.005, 'beg': 4, 'end': 6},
        ]
        self.assertFloatArray(converter.values('三割二部五厘'), expect)

        expect = [
            {'val': 0.123, 'beg': 2, 'end': 6},
        ]
        self.assertFloatArray(converter.values('多分.123です。'), expect)

        expect = [
            {'val': 0.00123, 'beg': 2, 'end': 8},
        ]
        self.assertFloatArray(converter.values('多分.00123です。'), expect)

    def test_values_kannsuuji(self):
        expect = [
            {'val': 1, 'beg': 0, 'end': 1},
            {'val': 2000000305017, 'beg': 6, 'end': 15},
        ]
        self.assertEqual(converter.values('１つの価格が二兆30万五千十7円になります。'), expect)

        expect = [
            {'val': 250, 'beg': 0, 'end': 4},
        ]
        self.assertEqual(converter.values('二百五十円'), expect)

        expect = [
            {'val': 1007, 'beg': 0, 'end': 2},
        ]
        self.assertEqual(converter.values('千七円'), expect)

        expect = [
            {'val': 120052, 'beg': 3, 'end': 9},
        ]
        self.assertEqual(converter.values('価格は十二万五十二円になります。'),  expect)

        expect = [
            {'val': 12000000000052, 'beg': 3, 'end': 9},
        ]
        self.assertEqual(converter.values('価格は十二兆五十二'), expect)

        expect = [
            {'val': 1001000000000052, 'beg': 0, 'end': 6},
        ]
        self.assertEqual(converter.values('千一兆五十二円になります。'), expect)

        expect = [
            {'val': 604002005, 'beg': 0, 'end': 9},
        ]
        self.assertEqual(converter.values('6億400万2千5になります。'), expect)

        expect = [
            {'val': 11010, 'beg': 0, 'end': 3},
        ]
        self.assertEqual(converter.values('万千十'),  expect)
