from datetime import datetime as dt
from datetime import timedelta as td
from collections import namedtuple

ISO_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
YMD_DATETIME_FORMAT = "%Y-%m-%d"


def get_billing_calendar(billing_date):

    """
    Generates a billing calendar based on the billing date.
    The generation assumes that the billing date is always the last day of the month and the billing period
    goes from the first day to the last day of the month
    """
    current_month_last_day = dt.strptime(billing_date, YMD_DATETIME_FORMAT)
    current_month_first_day = dt(year=current_month_last_day.year, month=current_month_last_day.month, day=1)
    prev_months_last_day = current_month_first_day - td(days=1)
    prev_months_first_day = dt(year=prev_months_last_day.year, month=prev_months_last_day.month, day=1)
    return BillingCalendar(prev_months_first_day,
                           prev_months_last_day,
                           current_month_first_day,
                           current_month_last_day,
                           current_month_last_day.day)


BillingCalendar = namedtuple('BillingCalendar', 'previous_month_first_day previous_month_last_day '
                                                'current_month_first_day current_month_last_day days_in_current_month')
