from datetime import datetime, tzinfo

from Resource.enumerations import Interval


class Quote:

    def __init__(self, quote):
        self.start = quote["start"]
        self.end = quote["end"]
        self.low = quote["low"]
        self.high = quote["high"]
        self.open = quote["open"]
        self.close = quote["close"]
        self.volume = quote["volume"]


class Time:

    def __init__(self, year, month, day, hour=0, min=0, sec=0,
                 interval=Interval.OneDay):
        self.date = datetime(year, month, day, hour, min, sec)
        self.interval = interval

    def __repr__(self):
        return self.date.isoformat() + "-05:00"

    def __add__(self, b):
        newDate = self.date + b * self.interval.delta
        newTime = Time(1, 1, 1, interval=self.interval)
        newTime.date = newDate
        return newTime

    def __iadd__(self, b):
        self.date += b * self.interval.delta
        return self

    def __lt__(self, b):
        return self.date < b

    def __le__(self, b):
        return self.date <= b

    def __eq__(self, b):
        return self.date == b

    def __ne__(self, b):
        return self.date != b

    def __gt__(self, b):
        return self.date > b

    def __ge__(self, b):
        return self.date >= b
