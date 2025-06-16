def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    return amount

def format_currency(amount):
    return "${:,.2f}".format(amount)