import argparse
import math


def calculate_differentiated_payments(principal, periods, interest):
    total_payment = 0
    for month in range(1, periods + 1):
        payment = math.ceil(principal / periods + interest * (principal - principal * (month - 1) / periods))
        total_payment += payment
        print(f"Month {month}: payment is {payment}")
    overpayment = total_payment - principal
    print(f"\nOverpayment = {overpayment}")


def calculate_annuity_payment(principal, periods, interest):
    annuity_payment = math.ceil(
        principal * (interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1))
    total_payment = annuity_payment * periods
    overpayment = total_payment - principal
    print(f"Your monthly payment = {annuity_payment}!\nOverpayment = {overpayment}")


def calculate_principal(payment, periods, interest):
    principal = payment / ((interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1))
    total_payment = payment * periods
    overpayment = total_payment - principal
    print(f"Your loan principal = {principal}!\nOverpayment = {overpayment}")


def calculate_periods(principal, payment, interest):
    periods = math.ceil(math.log(payment / (payment - interest * principal), 1 + interest))
    total_payment = payment * periods
    overpayment = total_payment - principal
    years = periods // 12
    months = periods % 12
    if years == 0:
        print(f"It will take {months} months to repay this loan!\nOverpayment = {overpayment}")
    elif months == 0:
        print(f"It will take {years} years to repay this loan!\nOverpayment = {overpayment}")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!\nOverpayment = {overpayment}")


parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--principal", type=int)
parser.add_argument("--payment", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()

if args.interest is None:
    print('Incorrect parameters')
elif args.interest is not None:
    if args.type == "diff":
        calculate_differentiated_payments(args.principal, args.periods, args.interest / (12 * 100))
    else:
        if args.principal is None:
            calculate_principal(args.payment, args.periods, args.interest / (12 * 100))
        elif args.periods is None:
            calculate_periods(args.principal, args.payment, args.interest / (12 * 100))
        else:
            calculate_annuity_payment(args.principal, args.periods, args.interest / (12 * 100))
