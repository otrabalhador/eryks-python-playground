class DatePattern(object):
    def __init__(self, year, month, day, weekday=0):
        self.year = year
        self.month = month
        self.day = day
        self.weekday = weekday
        pass

    def matches(self, date):
        return (
            self._year_matches(date) and
            self._month_matches(date) and
            self._day_matches(date) and
            self._weekday_matches(date)
        )

    def _year_matches(self, date):
        if not self.year:
            return True
        return self.year == date.year

    def _month_matches(self, date):
        if not self.month:
            return True
        return self.month == date.month

    def _day_matches(self, date):
        if not self.day:
            return True
        return self.day == date.day

    def _weekday_matches(self, date):
        if not self.weekday:
            return True
        return self.weekday == date.weekday()