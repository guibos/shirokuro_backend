import datetime


class DatetimeType(datetime.datetime):
    @classmethod
    def from_datetime(cls, dt: datetime.datetime) -> 'DatetimeType':
        return cls(year=dt.year, month=dt.month, day=dt.day, hour=dt.hour, minute=dt.minute, second=dt.second,
                   microsecond=dt.microsecond, tzinfo=dt.tzinfo, fold=dt.fold)

    def to_datetime(self) -> datetime.datetime:
        return datetime.datetime(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second,
                   microsecond=self.microsecond, tzinfo=self.tzinfo, fold=self.fold)

