import inspect
import unittest

from suji.converter import values, value


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

    def test_empty_0(self):
        self.assertEqual(value(''), '')

    def test_empty_1(self):
        self.assertEqual(value('こんにちは'), 'こんにちは')

    def test_empty_2(self):
        self.assertEqual(values(''), [])

    def test_empty_3(self):
        self.assertEqual(values('こんにちは'), [])

    def test_values_int_000(self):
        expect = [
            {'val': 5, 'beg': 0, 'end': 1}
        ]
        self.assertEqual(values('５'), expect)

    def test_values_int_001(self):
        expect = [
            {'val': 5, 'beg': 3, 'end': 4}
        ]
        self.assertEqual(values('これは5円です。'), expect)

    def test_values_int_002(self):
        expect = [
            {'val': 1000, 'beg': 3, 'end': 8}
        ]
        self.assertEqual(values('これは1,000円です。'), expect)

    def test_values_int_003(self):
        expect = [
            {'val': 2, 'beg': 2, 'end': 3}
        ]
        self.assertEqual(values('値は2'), expect)

    def test_values_int_004(self):
        expect = [
            {'val': 3000, 'beg': 2, 'end': 7}
        ]
        self.assertEqual(values('値は3,000'), expect)

    def test_values_int_005(self):
        expect = [
            {'val': 400, 'beg': 0, 'end': 4}
        ]
        self.assertEqual(values('400, 円になります。'), expect)

    def test_values_int_006(self):
        expect = [
            {'val': 1000, 'beg': 0, 'end': 6},
            {'val': 2000, 'beg': 7, 'end': 13},
            {'val': 3000, 'beg': 14, 'end': 20},
        ]
        self.assertEqual(values('1,000, 2,000, 3,000,'), expect)

    def test_values_int_007(self):
        expect = [
            {'val': 5, 'beg': 3, 'end': 4},
            {'val': 60, 'beg': 5, 'end': 7},
            {'val': 700, 'beg': 8, 'end': 11},
        ]
        self.assertEqual(values('数列、5、60、700、'), expect)

    def test_values_decimal_000(self):
        expect = [
            {'val': 0.6, 'beg': 0, 'end': 3},
        ]
        self.assertFloatArray(values('0.6'), expect)

    def test_values_decimal_001(self):
        expect = [
            {'val': 0.0007, 'beg': 0, 'end': 6},
        ]
        self.assertFloatArray(values('0.0007'), expect)

    def test_values_decimal_002(self):
        expect = [
            {'val': 0.987654321, 'beg': 0, 'end': 11},
        ]
        self.assertFloatArray(values('0.987654321'), expect)

    def test_values_decimal_003(self):
        expect = [
            {'val': 1.3, 'beg': 0, 'end': 3},
        ]
        self.assertFloatArray(values('1.3'), expect)

    def test_values_decimal_004(self):
        expect = [
            {'val': 123.45, 'beg': 0, 'end': 6},
        ]
        self.assertFloatArray(values('123.45'), expect)

    def test_values_decimal_005(self):
        expect = [
            {'val': 1, 'beg': 0, 'end': 2},
        ]
        self.assertFloatArray(values('1.'), expect)

    def test_values_decimal_006(self):
        expect = [
            {'val': 1, 'beg': 3, 'end': 5},
        ]
        self.assertFloatArray(values('これは1.です。'), expect)

    def test_values_decimal_007(self):
        expect = [
            {'val': 0.325, 'beg': 0, 'end': 6},
        ]
        self.assertFloatArray(values('三割二分五厘'), expect)

    def test_values_decimal_008(self):
        expect = [
            {'val': 2.3, 'beg': 0, 'end': 3},
            {'val': 0.005, 'beg': 4, 'end': 6},
        ]
        self.assertFloatArray(values('三割二部五厘'), expect)

    def test_values_decimal_009(self):
        expect = [
            {'val': 0.123, 'beg': 2, 'end': 6},
        ]
        self.assertFloatArray(values('多分.123です。'), expect)

    def test_values_decimal_010(self):
        expect = [
            {'val': 0.00123, 'beg': 2, 'end': 8},
        ]
        self.assertFloatArray(values('多分.00123です。'), expect)

    def test_values_kansuji_000(self):
        expect = [
            {'val': 250, 'beg': 0, 'end': 4},
        ]
        self.assertEqual(values('二百五十円'), expect)

    def test_values_kansuji_001(self):
        expect = [
            {'val': 1007, 'beg': 0, 'end': 2},
        ]
        self.assertEqual(values('千七円'), expect)

    def test_values_kansuji_002(self):
        expect = [
            {'val': 1000, 'beg': 0, 'end': 2},
        ]
        self.assertEqual(values('一千'), expect)

    def test_values_kansuji_003(self):
        expect = [
            {'val': 10000000, 'beg': 0, 'end': 3},
        ]
        self.assertEqual(values('一千万円'), expect)

    def test_values_kansuji_004(self):
        expect = [
            {'val': 11110000, 'beg': 0, 'end': 8},
        ]
        self.assertEqual(values('一千一百一十一万円'), expect)

    def test_values_kansuji_005(self):
        expect = [
            {'val': 11110000, 'beg': 3, 'end': 11},
        ]
        self.assertEqual(values('価格は一千一百一十一万'), expect)

    def test_values_kansuji_006(self):
        expect = [
            {'val': 11110000, 'beg': 3, 'end': 11},
        ]
        self.assertEqual(values('価格は一千一百一十一万円です。'), expect)

    def test_values_kansuji_007(self):
        expect = [
            {'val': 11100000, 'beg': 0, 'end': 4},
        ]
        self.assertEqual(values('千百十万円'), expect)

    def test_values_kansuji_008(self):
        expect = [
            {'val': 12130000, 'beg': 0, 'end': 6},
        ]
        self.assertEqual(values('千二百十三万円'), expect)

    def test_values_kansuji_009(self):
        expect = [
            {'val': 91180000, 'beg': 0, 'end': 6},
        ]
        self.assertEqual(values('九千百十八万円'), expect)

    def test_values_kansuji_010(self):
        expect = [
            {'val': 11101111, 'beg': 0, 'end': 8},
        ]
        self.assertEqual(values('千百十万千百十一円'), expect)

    def test_values_kansuji_011(self):
        expect = [
            {'val': 120052, 'beg': 3, 'end': 9},
        ]
        self.assertEqual(values('価格は十二万五十二円になります。'),  expect)

    def test_values_kansuji_012(self):
        expect = [
            {'val': 12000000000052, 'beg': 3, 'end': 9},
        ]
        self.assertEqual(values('価格は十二兆五十二'), expect)

    def test_values_kansuji_013(self):
        expect = [
            {'val': 1001000000000052, 'beg': 0, 'end': 6},
        ]
        self.assertEqual(values('千一兆五十二円になります。'), expect)

    def test_values_kansuji_014(self):
        expect = [
            {'val': 604002005, 'beg': 0, 'end': 9},
        ]
        self.assertEqual(values('6億400万2千5になります。'), expect)

    def test_values_kansuji_015(self):
        expect = [
            {'val': 11110, 'beg': 0, 'end': 4},
        ]
        self.assertEqual(values('万千百十'),  expect)

    def test_values_kansuji_016(self):
        expect = [
            {'val': 1, 'beg': 0, 'end': 1},
            {'val': 2000000305017, 'beg': 6, 'end': 15},
        ]
        self.assertEqual(values('１つの価格が二兆30万五千十7円になります。'), expect)

    def test_value_000(self):
        self.assertEqual(value('二百五十円'), '250円')

    def test_value_001(self):
        self.assertEqual(value('千七円'), '1007円')

    def test_value_002(self):
        self.assertEqual(value('一千'), '1000')

    def test_value_003(self):
        self.assertEqual(value('一千万円'), '10000000円')

    def test_value_004(self):
        self.assertEqual(value('一千一百一十一万円'), '11110000円')

    def test_value_005(self):
        self.assertEqual(value('3億'), '300000000')

    def test_value_006(self):
        self.assertEqual(value('価格は一千一百一十一万'), '価格は11110000')

    def test_value_007(self):
        self.assertEqual(value('価格は一千一百一十一万円です。'), '価格は11110000円です。')

    def test_value_008(self):
        self.assertEqual(value('千百十万円'), '11100000円')

    def test_value_009(self):
        self.assertEqual(value('千二百十三万円'), '12130000円')

    def test_value_010(self):
        self.assertEqual(value('九千百十八万円'), '91180000円')

    def test_value_011(self):
        self.assertEqual(value('千百十万千百十一円'), '11101111円')

    def test_value_012(self):
        self.assertEqual(value('価格は十二万五十二円になります。'),  '価格は120052円になります。')

    def test_value_013(self):
        self.assertEqual(value('価格は十二兆五十二'), '価格は12000000000052')

    def test_value_014(self):
        self.assertEqual(value('千一兆五十二円になります。'), '1001000000000052円になります。')

    def test_value_015(self):
        self.assertEqual(value('6億400万2千5になります。'), '604002005になります。')

    def test_value_016(self):
        self.assertEqual(value('万千百十'), '11110')

    def test_value_017(self):
        self.assertEqual(value('１つの価格が二兆30万五千十7円になります。'), '1つの価格が2000000305017円になります。')

    def test_value_018(self):
        self.assertEqual(value('16兆８千億ドル'), '16800000000000ドル')
