import unittest
from datetime import datetime as dt
from bill_member import calculate_bill, get_reading_in_range, get_monthly_readings
from billing_calendar import BillingCalendar


class TestBillMember(unittest.TestCase):

    def test_calculate_bill_for_ALL_for_august(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='ALL',
                                     bill_date='2017-08-31')
        self.assertEqual(amount, 27.57)
        self.assertEqual(kwh, 167)

    def test_calculate_bill_for_ALL_first_month(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='ALL',
                                     bill_date='2017-03-28')
        self.assertEqual(amount, 2107.51)
        self.assertEqual(kwh, 17580)

    def test_calculate_bill_for_ALL_unknown_month(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='ALL',
                                     bill_date='2022-12-31')
        self.assertEqual(amount, 7.61)
        self.assertEqual(kwh, 0)

    def test_calculate_bill_for_account_abc_for_august(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='account-abc',
                                     bill_date='2017-08-31')
        self.assertEqual(amount, 27.57)
        self.assertEqual(kwh, 167)

    def test_calculate_bill_for_account_abc_first_month(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='ALL',
                                     bill_date='2017-03-28')
        self.assertEqual(amount, 2107.51)
        self.assertEqual(kwh, 17580)

    def test_calculate_bill_for_account_abc_unknown_month(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='account-abc',
                                     bill_date='2022-12-31')
        self.assertEqual(amount, 7.61)
        self.assertEqual(kwh, 0)

    def test_calculate_bill_for_invalid_account_for_august(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='account-abcd',
                                     bill_date='2017-08-31')
        self.assertEqual(amount, 0)
        self.assertEqual(kwh, 0)

    def test_calculate_bill_for_invalid_account_first_month(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='account-abcd',
                                     bill_date='2017-03-28')
        self.assertEqual(amount, 0)
        self.assertEqual(kwh, 0)

    def test_calculate_bill_for_invalid_account_for_unknown_month(self):
        amount, kwh = calculate_bill(member_id='member-123',
                                     account_id='account-abcd',
                                     bill_date='2022-12-31')
        self.assertEqual(amount, 0)
        self.assertEqual(kwh, 0)

    def test_get_reading_in_range_returns_correct_value(self):
        readings = test_readings
        reading_of_range = get_reading_in_range(readings, dt(year=2017, month=4, day=1), dt(year=2017, month=4, day=30))
        self.assertEqual(
            {
                "cumulative": 17759,
                "readingDate": "2017-04-15T00:00:00.000Z",
                "unit": "kWh"
            }, reading_of_range)

    def test_get_reading_in_range_returns_empty_value(self):
        readings = test_readings
        reading_of_range = get_reading_in_range(readings, dt(year=2016, month=4, day=1), dt(year=2016, month=4, day=30))
        self.assertEqual({"cumulative": 0}, reading_of_range)

    def test_get_monthly_readings_returns_correct_prev_and_current_readings(self):
        test_billing_calendar = BillingCalendar(dt(2017, 3, 1), dt(2017, 3, 31), dt(2017, 4, 1), dt(2017, 4, 30), 30)
        readings = test_readings
        prev, current = get_monthly_readings(test_billing_calendar, readings)
        self.assertEqual(test_readings[0], prev)
        self.assertEqual(test_readings[1], current)

    def test_get_monthly_readings_returns_correct_prev_and_current_readings_missing_prev_month(self):
        test_billing_calendar = BillingCalendar(dt(2017, 2, 1), dt(2017, 2, 28), dt(2017, 3, 1), dt(2017, 3, 31), 31)
        readings = test_readings
        prev, current = get_monthly_readings(test_billing_calendar, readings)
        self.assertEqual({"cumulative": 0}, prev)
        self.assertEqual(test_readings[0], current)


test_readings = [{
    "cumulative": 17580,
    "readingDate": "2017-03-28T00:00:00.000Z",
    "unit": "kWh"
    },
    {
    "cumulative": 17759,
    "readingDate": "2017-04-15T00:00:00.000Z",
    "unit": "kWh"
    },
    {
    "cumulative": 18002,
    "readingDate": "2017-05-08T00:00:00.000Z",
    "unit": "kWh"
}]
