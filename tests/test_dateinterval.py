from typing import Iterable, Iterable
from datetime import datetime, date, timedelta
from dateinterval import *
from itertools import chain


def generate_date_ranges():
    p1 = list(generate_interval_date_ranges(
        date(2021, 5, 1), td=timedelta(days=1), steps=3))
    p2 = list(generate_interval_date_ranges(
        date(2021, 6, 1), td=timedelta(days=1), steps=4))
    p3 = list(generate_interval_date_ranges(
        date(2021, 7, 1), td=timedelta(days=1), steps=5))

    return chain.from_iterable([p1, p2, p3])

def test_hourly_interval():
    d = list(generate_interval_date_ranges(
        datetime(2021, 5, 1), td=timedelta(hours=6), steps=8))
    
    d.extend(generate_interval_date_ranges(
        datetime(2021, 8, 9), td=timedelta(hours=6), steps=8))
    
    expected = [
        [datetime(2021, 5, 1, 0, 0), datetime(2021, 5, 3, 0, 0)], 
        [datetime(2021, 8, 9, 0, 0), datetime(2021, 8, 11, 0, 0)]
    ]

    actual = summarize_date_ranges(d, gap_toleration=timedelta(hours=6))

    assert expected == actual


def test_inverse_interval_generation():
    actual = summarize_date_ranges(generate_date_ranges(), only_missing=True)
    expected = [
        [date(2021, 5, 5), date(2021, 5, 31)], 
        [date(2021, 6, 6), date(2021, 6, 30)]
    ]
    assert expected == actual

def test_interval_generation():
    actual = summarize_date_ranges(generate_date_ranges())
    expected = [
        [date(2021, 5, 1), date(2021, 5, 4)], 
        [date(2021, 6, 1), date(2021, 6, 5)], 
        [date(2021, 7, 1), date(2021, 7, 6)]
    ]
    assert expected == actual

def test_coherence_of_inversion():
    left = summarize_date_ranges(generate_date_ranges())
    right = summarize_date_ranges(generate_date_ranges(), only_missing=True)

    l = sorted(left + right)

    for i, v in enumerate(l): 
        if i == 0:
            continue
        assert (v[0] - timedelta(1)) == l[i - 1][1]
