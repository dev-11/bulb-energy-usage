def get_accounts(account_id):
    if account_id == 'ALL':
        return ['electricity', 'gas']
    elif account_id == 'electricity':
        return ['electricity']
    elif account_id == 'gas':
        return ['gas']
    else:
        return []
