# failUnless = assertTrue
# failIf = assertFalse

import datetime
import unittest

from date.date_pattern import DatePattern


class DatePatternTests(unittest.TestCase):
    def test_matches_true(self):
        actual = DatePattern(2017, 10, 10)
        expected = datetime.date(2017, 10, 10)
        self.assertTrue(actual.matches(expected))

    def test_matches_false(self):
        actual = DatePattern(2017, 10, 10)
        expected = datetime.date(2017, 10, 11)
        self.assertFalse(actual.matches(expected))

    def test_matches_year_as_wild_card(self):
        actual = DatePattern(0, 10, 10)
        expected = datetime.date(2017, 10, 10)
        self.assertTrue(actual.matches(expected))

    def test_matches_month_as_wild_card(self):
        actual = DatePattern(0, 0, 10)
        expected = datetime.date(2017, 10, 10)
        self.assertTrue(actual.matches(expected))

    def test_matches_weekday(self):
        actual = DatePattern(0, 0, 0, 2) # 2 is Weekday
        expected = datetime.date(2004, 9, 29)
        self.assertTrue(actual.matches(expected))


if __name__ == '__main__':
    unittest.main()
