from load_readings import get_readings
from datetime import datetime as dt
import datetime_utils as dtu
import tariff


def calculate_bill(member_id=None, account_id=None, bill_date=None):

    billing_calendar = dtu.get_billing_calendar(bill_date)
    data = get_readings()
    bills = []

    readings = list(get_readings_by_account_id(account_id, data[member_id]))

    for reading in readings:
        for energy_type in reading:
            bill = get_bill_by_account(energy_type, billing_calendar, reading[energy_type])
            bills.append(bill)

    return 0, 0 if len(bills) >= 0 else [sum(x) for x in zip(*bills)]


def get_readings_by_account_id(account_id, readings):
    if account_id == 'ALL':
        for account_list in readings:
            for account in account_list:
                for energy_types in account_list[account]:
                    yield energy_types

    for account_list in readings:
        for account in account_list:
            if account_id == account:
                for energy_types in account_list[account]:
                    yield energy_types


def get_bill_by_account(energy_type, billing_calendar, data):

    previous, current = get_readings_by_account(billing_calendar, data)
    consumption = current['cumulative'] - previous['cumulative']
    consumption_cost = (consumption * tariff.BULB_TARIFF[energy_type]['unit_rate']) / 100
    monthly_standing_charge = (billing_calendar.days_in_current_month
                               * tariff.BULB_TARIFF[energy_type]['standing_charge']) / 100
    return round(consumption_cost + monthly_standing_charge, 2), consumption


def get_reading(readings, first_day, last_day):
    reading = list(filter(lambda x: first_day <= dt.strptime(x['readingDate'], dtu.ISO_DATETIME_FORMAT) <= last_day,
                          readings))

    return {'cumulative': 0} if len(reading) == 0 else reading[0]


def get_readings_by_account(billing_calendar, data):

    current = get_reading(data, billing_calendar.current_month_first_day, billing_calendar.current_month_last_day)
    previous = get_reading(data, billing_calendar.previous_month_first_day, billing_calendar.previous_month_last_day)

    return previous, current


def calculate_and_print_bill(member_id, account, bill_date):
    """Calculate the bill and then print it to screen.
    Account is an optional argument - I could bill for one account or many.
    There's no need to refactor this function."""
    member_id = member_id or 'member-123'
    bill_date = bill_date or '2017-08-31'
    account = account or 'ALL'
    amount, kwh = calculate_bill(member_id, account, bill_date)
    print('Hello {member}!'.format(member=member_id))
    print('Your bill for {account} on {date} is £{amount}'.format(
        account=account,
        date=bill_date,
        amount=amount))
    print('based on {kwh}kWh of usage in the last month'.format(kwh=kwh))
