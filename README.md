# Bulb energy usage

[![Build Status](https://travis-ci.org/dev-11/bulb-energy-usage.svg?branch=master)](https://travis-ci.org/dev-11/bulb-energy-usage)
[![codecov](https://codecov.io/gh/dev-11/bulb-energy-usage/branch/master/graph/badge.svg)](https://codecov.io/gh/dev-11/bulb-energy-usage)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6f88c1e279884955b167a9a94b6530b4)](https://www.codacy.com/manual/dev-11/bulb-energy-usage?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dev-11/bulb-energy-usage&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/6f88c1e279884955b167a9a94b6530b4)](https://www.codacy.com/manual/dev-11/bulb-energy-usage?utm_source=github.com&utm_medium=referral&utm_content=dev-11/bulb-energy-usage&utm_campaign=Badge_Coverage)

## The approach
I've tried to brake down the bill calculation to smaller sub-tasks.

These are the bits what I've identified.

1.  We need a calendar and calendar related functions to generate a bill
2.  We need to narrow down the received data by the `member_id`
3.  We need to narrow down the received data by the `account_id`
4.  We need to be able to select readings based on the given billing month.
5.  We need to identify each reading by its energy type to calculate the correct tariff.

### bill_member.py

#### calculate_bill

This the provided method which server some sort of controller functionality to control the bill calculation workflow and pull every information together. 

#### get_readings_by_account_id

This method uses the whole reading list of the member and will return simple list of the readings with the energy type of the readings. It doesn't change the data structure, just narrows down the reading set to the relevant readings. 

#### get_bill_by_energy_type

Because the energy type determines the tariff and the final bill, I've introduced this method to calculate a sub-bill. Like an account with electricity and gas readings can have two sub-bills. One for the electricity and one for the gas.

#### get_reading_in_range

This method selects the reading from a date range. This is important because we have to find, for instance, the current reading to calculate the bill.

#### get_monthly_readings

This method receives the billing date and based on that it will return the reading of the billing month and the previous month's reading.

### billing_calendar.py

This brand new file holds every logic to handle the calendar related functionality. To calculate a bill we need to know the previous month (to get its reading), the current month (to get the current reading), and the number of days in the current month to calculate the standing charge for the month. 

#### get_billing_calendar

This method returns a `BillingCalendar` tuple which will contain all the five calendar related information to calculate the bill. 

### Improvements

-   Right now the calculation doesn't detail the bill. It would be good to see a bill breakdown by energy type or make it possible to calculate only gas or electricity bill.
-   The incoming data from the json is also a little bit strange. It makes it possible to have duplicate account ids and duplicate energy types, which raises a few questions.
-   The path of the json file is baked into the code. 
