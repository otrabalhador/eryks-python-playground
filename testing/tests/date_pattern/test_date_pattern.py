# failUnless = assertTrue
# failIf = assertFalse

import datetime
import unittest

from date.composite_pattern import CompositePattern
from date.day_pattern import DayPattern
from date.month_pattern import MonthPattern
from date.weekday_pattern import WeekdayPattern
from date.year_pattern import YearPattern
from date.last_weekday_pattern import LastWeekdayPattern

MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(0, 7)


class DatePatternTests(unittest.TestCase):
    def setUp(self):
        self.date = datetime.date(2004, 9, 29)

    def test_year_pattern_matches(self):
        year_pattern = YearPattern(2004)
        self.assertTrue(year_pattern.matches(self.date))

    def test_year_pattern_does_not_match(self):
        year_pattern = YearPattern(2005)
        self.assertFalse(year_pattern.matches(self.date))

    def test_month_pattern_matches(self):
        month_pattern = MonthPattern(9)
        self.assertTrue(month_pattern.matches(self.date))

    def test_month_pattern_does_not_match(self):
        month_pattern = MonthPattern(11)
        self.assertFalse(month_pattern.matches(self.date))

    def test_day_pattern_matches(self):
        day_pattern = DayPattern(29)
        self.assertTrue(day_pattern.matches(self.date))

    def test_day_pattern_does_not_match(self):
        day_pattern = DayPattern(21)
        self.assertFalse(day_pattern.matches(self.date))

    def test_weekday_pattern_matches(self):
        weekday_pattern = WeekdayPattern(2)  # Wednesday
        self.assertTrue(weekday_pattern.matches(self.date))

    def test_weekday_pattern_does_not_match(self):
        weekday_pattern = WeekdayPattern(1)  # Tuesday
        self.assertFalse(weekday_pattern.matches(self.date))

    def test_composite_matches(self):
        cp = CompositePattern()
        cp.add(YearPattern(2004))
        cp.add(MonthPattern(9))
        cp.add(DayPattern(29))
        self.assertTrue(cp.matches(self.date))

    def test_composite_does_not_match(self):
        cp = CompositePattern()
        cp.add(YearPattern(2004))
        cp.add(MonthPattern(9))
        cp.add(DayPattern(30))
        self.assertFalse(cp.matches(self.date))

    def test_composite_without_year_matches(self):
        cp = CompositePattern()
        cp.add(MonthPattern(9))
        cp.add(DayPattern(29))
        self.assertTrue(cp.matches(self.date))


class LastWeekdayPatternTests(unittest.TestCase):
    def setUp(self):
        self.pattern = LastWeekdayPattern(WEDNESDAY)

    def test_last_wednesday_matches(self):
        last_wed_of_sept_2004 = datetime.date(2004, 9, 29)
        self.assertTrue(self.pattern.matches(last_wed_of_sept_2004))

    def test_last_wednesday_does_not_match(self):
        first_wed_of_sept_2004 = datetime.date(2004, 9, 1)
        self.assertFalse(self.pattern.matches(first_wed_of_sept_2004))


if __name__ == '__main__':   unittest.main()
