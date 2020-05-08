import unittest
import billing_calendar as bc
from _datetime import datetime as dt
from parameterized import parameterized


class TestBillingCalendar(unittest.TestCase):
    def test_get_billing_calendar_january_returns_correct_calendar(self):
        date = '2020-01-31'
        calendar = bc.get_billing_calendar(date)
        self.assertEqual(dt(2020,  1,  1), calendar.current_month_first_day)
        self.assertEqual(dt(2020,  1, 31), calendar.current_month_last_day)
        self.assertEqual(dt(2019, 12,  1), calendar.previous_month_first_day)
        self.assertEqual(dt(2019, 12, 31), calendar.previous_month_last_day)
        self.assertEqual(31, calendar.days_in_current_month)

    def test_get_billing_calendar_leap_year_feb_returns_correct_calendar(self):
        date = '2020-02-29'
        calendar = bc.get_billing_calendar(date)
        self.assertEqual(dt(2020, 2,  1), calendar.current_month_first_day)
        self.assertEqual(dt(2020, 2, 29), calendar.current_month_last_day)
        self.assertEqual(dt(2020, 1,  1), calendar.previous_month_first_day)
        self.assertEqual(dt(2020, 1, 31), calendar.previous_month_last_day)
        self.assertEqual(29, calendar.days_in_current_month)

    def test_get_billing_calendar_not_leap_year_feb_returns_correct_calendar(self):
        date = '2019-02-28'
        calendar = bc.get_billing_calendar(date)
        self.assertEqual(dt(2019, 2,  1), calendar.current_month_first_day)
        self.assertEqual(dt(2019, 2, 28), calendar.current_month_last_day)
        self.assertEqual(dt(2019, 1,  1), calendar.previous_month_first_day)
        self.assertEqual(dt(2019, 1, 31), calendar.previous_month_last_day)
        self.assertEqual(28, calendar.days_in_current_month)

    def test_get_billing_calendar_leap_year_march_returns_correct_calendar(self):
        date = '2020-03-31'
        calendar = bc.get_billing_calendar(date)
        self.assertEqual(dt(2020, 3,  1), calendar.current_month_first_day)
        self.assertEqual(dt(2020, 3, 31), calendar.current_month_last_day)
        self.assertEqual(dt(2020, 2,  1), calendar.previous_month_first_day)
        self.assertEqual(dt(2020, 2, 29), calendar.previous_month_last_day)
        self.assertEqual(31, calendar.days_in_current_month)

    def test_get_billing_calendar_not_leap_year_march_returns_correct_calendar(self):
        date = '2019-03-31'
        calendar = bc.get_billing_calendar(date)
        self.assertEqual(dt(2019, 3,  1), calendar.current_month_first_day)
        self.assertEqual(dt(2019, 3, 31), calendar.current_month_last_day)
        self.assertEqual(dt(2019, 2,  1), calendar.previous_month_first_day)
        self.assertEqual(dt(2019, 2, 28), calendar.previous_month_last_day)
        self.assertEqual(31, calendar.days_in_current_month)

    def test_get_billing_calendar_november_returns_correct_calendar(self):
        date = '2020-11-30'
        calendar = bc.get_billing_calendar(date)
        self.assertEqual(dt(2020, 11,  1), calendar.current_month_first_day)
        self.assertEqual(dt(2020, 11, 30), calendar.current_month_last_day)
        self.assertEqual(dt(2020, 10,  1), calendar.previous_month_first_day)
        self.assertEqual(dt(2020, 10, 31), calendar.previous_month_last_day)
        self.assertEqual(30, calendar.days_in_current_month)

    @parameterized.expand([
        ["bad_leap_yar", '2019-02-29', ValueError],
        ["bad_last_day_november", '2020-11-31', ValueError],
        ["bad_last_day_october", '2020-10-32', ValueError],
        ["not_a_date_string", 'asdfasdfasd', ValueError],
        ["empty_string", '', ValueError],
        ["None", None, TypeError]
    ])
    def test_get_billing_bad_day_returns_correct_calendar(self, name, date, error):
        self.assertRaises(error, bc.get_billing_calendar, date)
