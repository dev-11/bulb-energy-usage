import unittest

from bill_member import calculate_bill


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
