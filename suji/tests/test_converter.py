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
            self.assertAlmostEqual(actual[i], expected[i], msg=m)

    def test_values_int(self):
        self.assertEqual(converter.values('こんにちは'), [])
        self.assertEqual(converter.values('これは5円です。'), [5])
        self.assertEqual(converter.values('これは1,000円です。'), [1000])
        self.assertEqual(converter.values('値は2'), [2])
        self.assertEqual(converter.values('値は3,000'), [3000])
        self.assertEqual(converter.values('400, 円になります。'), [400])
        self.assertEqual(converter.values('1,000, 2,000, 3,000,'), [1000, 2000, 3000])
        self.assertEqual(converter.values('数列、5、60、700、'), [5, 60, 700])

    def test_values_deciaml(self):
        self.assertFloatArray(converter.values('0.6'), [float(0.6)])
        self.assertFloatArray(converter.values('0.0007'), [0.0007])
        self.assertFloatArray(converter.values('0.987654321'), [0.987654321])
        self.assertFloatArray(converter.values('1.3'), [1.3])
        self.assertFloatArray(converter.values('123.45'), [123.45])
        self.assertFloatArray(converter.values('1.'), [1])
        self.assertFloatArray(converter.values('これは1.です。'), [1])
        self.assertFloatArray(converter.values('三割二分五厘'), [0.325])
        self.assertFloatArray(converter.values('三割二部五厘'), [2.3, 0.005])

    def test_values_kannsuuji(self):
        self.assertEqual(converter.values('二兆30万五千十7'), [2000000305017])
        self.assertEqual(converter.values('二百五十円'), [250])
        self.assertEqual(converter.values('千七円'), [1007])
        self.assertEqual(converter.values('価格は十二万五十二円になります。'), [120052])
        self.assertEqual(converter.values('価格は十二兆五十二'), [12000000000052])
        self.assertEqual(converter.values('千一兆五十二円になります。'), [1001000000000052])
        self.assertEqual(converter.values('6億400万2千5になります。'), [604002005])
        self.assertEqual(converter.values('万千十'), [11010])
