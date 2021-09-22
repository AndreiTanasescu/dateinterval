# dateinterval
Summarize lists of dates with intervals

* [Readthedocs : https://dateinterval.readthedocs.io](https://dateinterval.readthedocs.io)
* [PyPi : https://pypi.org/project/dateinterval/](https://pypi.org/project/dateinterval/)

```
>>> from datetime import timedelta, date
>>> from dateinterval import *
>>> d = dateinterval.generate_interval_date_ranges(date(2021,1,1), td=timedelta(days=1), steps=3)
>>> print(dateinterval.summarize_date_ranges(d))
[[datetime.date(2021, 1, 1), datetime.date(2021, 1, 4)]]
>>>
```