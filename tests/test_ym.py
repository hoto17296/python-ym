from unittest import TestCase
from datetime import date, datetime
from ym import ym


class TestYm(TestCase):
    def testInit(self):
        x202004 = 2020 * 12 + 4 - 1
        self.assertEqual(ym(2020, 4).x, x202004)
        self.assertEqual(ym((2020, 4)).x, x202004)
        self.assertEqual(ym([2020, 4]).x, x202004)
        self.assertEqual(ym(date(2020, 4, 1)).x, x202004)
        self.assertEqual(ym(datetime(2020, 4, 1)).x, x202004)
        self.assertEqual(ym("2020-04").x, x202004)
        self.assertEqual(ym(x202004).x, x202004)
        self.assertEqual(ym(ym(x202004)).x, x202004)

    def testCurrent(self):
        current = ym.current()
        today = date.today()
        self.assertIsInstance(current, ym)
        self.assertEqual(current.y, today.year)
        self.assertEqual(current.m, today.month)

    def testOperation(self):
        self.assertEqual(ym(2020, 4) + 10, ym(2021, 2))
        self.assertEqual(ym(2020, 4) - 10, ym(2019, 6))
        self.assertEqual(ym(2020, 4) - ym(2019, 6), 10)
        self.assertTrue(ym(2020, 4) > ym(2020, 3))
        self.assertFalse(ym(2020, 4) < ym(2020, 3))
        self.assertTrue(ym(2020, 4) == ym(2020, 4))
        self.assertFalse(ym(2020, 4) == ym(2020, 3))

    def testStr(self):
        self.assertEqual(str(ym(2020, 4)), "2020-04")

    def testTo(self):
        self.assertListEqual(list(ym(2020, 4).to(2020, 7)), [ym(2020, 4), ym(2020, 5), ym(2020, 6)])
        self.assertListEqual(list(ym(2020, 4).to(2020, 3)), [])
