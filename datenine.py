class Date:
    def __init__(
        self,
        year: int = None,
        month: int = None,
        day: int = None,
        hour: int = None,
        minute: int = None,
        second: int = None,
    ):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def from_datetime(self, dt):
        self.year = dt.year
        self.month = dt.month
        self.day = dt.day
        self.hour = dt.hour
        self.minute = dt.minute
        self.second = dt.second

    def __repr__(self):
        return f"Date({self.year, self.month, self.day, self.hour, self.minute, self.second})"


d = Date()
print(repr(d))
