import re
from datetime import date, datetime


class ym:
    def __init__(self, a, b=None):
        if type(a) is self.__class__:
            y, m = a.y, a.m
        elif type(a) is int and type(b) is int:
            y, m = a, b
        elif type(a) in (date, datetime):
            y, m = a.year, a.month
        elif type(a) in (tuple, list) and type(a[0]) is type(a[1]) is int:
            y, m = a
        elif type(a) is str:
            matched = re.match(r"^(\d+)-(\d+)$", a)
            if matched:
                y, m = int(matched[1]), int(matched[2])
            else:
                raise ValueError()
        elif type(a) is int:
            y, m = a // 12, a % 12 + 1
        else:
            raise ValueError()
        if not (0 <= y <= 10000 and 1 <= m <= 12):
            raise ValueError()
        self.x = y * 12 + m - 1

    @classmethod
    def current(cls):
        return cls(date.today())

    @property
    def y(self) -> int:
        return self.x // 12

    @property
    def m(self) -> int:
        return self.x % 12 + 1

    def to(self, *args):
        target = self.__class__(*args)
        for i in range(target - self):
            yield self + i

    def __repr__(self):
        cls = self.__class__
        return f"{cls.__name__}({self.y}, {self.m})"

    def __str__(self):
        return f"{self.y:04d}-{self.m:02d}"

    def __add__(self, n: int):
        if type(n) is int:
            y, m = (self.x + n) // 12, (self.x + n) % 12 + 1
            return self.__class__((y, m))
        raise TypeError()

    def __sub__(self, other):
        if type(other) is int:
            return self + (-1 * other)
        if type(other) is self.__class__:
            return self.x - other.x
        raise TypeError()

    def __eq__(self, other):
        return self.x == other.x

    def __ne__(self, other):
        return self.x != other.x

    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.x > other.x
