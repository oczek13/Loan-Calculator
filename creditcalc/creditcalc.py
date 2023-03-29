import math
import argparse

parser = argparse.ArgumentParser('Loan Calculator')
parser.add_argument('-t', '--type', choices=["annuity", "diff"])
parser.add_argument('-p', '--payment', type=int, default=0)
parser.add_argument('-pr', '--principal', type=int, default=0)
parser.add_argument('-pe', '--periods', type=int, default=0)
parser.add_argument('-i', '--interest', type=float, default=0)

args = vars(parser.parse_args())

loan_type = args['type']
payment = args['payment']
principal = args['principal']
periods = args['periods']
interest = args['interest']

nominal_interest_rate = (interest/100)/12

if loan_type == 'diff':
    temp = principal / periods
    suma = 0
    for i in range(1, periods + 1):
        diff_payment = temp + nominal_interest_rate*(principal - ((principal * (i - 1))/periods))  # czy nawiasy dobrze?
        print("Month ", i, ": payment is ", math.ceil(diff_payment))
        suma = suma + math.ceil(diff_payment)
    print("Overpayment = ", suma - principal)

if loan_type == 'annuity':

    if principal == 0:
        temp = pow((1 + nominal_interest_rate), periods)
        loan_principal = payment / (nominal_interest_rate * temp / (temp - 1))
        print("Your loan principal = ", round(loan_principal), "!")
        overpayment = (payment * periods) - loan_principal
        print("Overpayment = ", overpayment)

    elif periods == 0:
        if interest == 0:
            print("Incorrect parameters")
        else:
            n = math.log(payment/(payment - (nominal_interest_rate * principal)), 1 + nominal_interest_rate)
            number_of_months = math.ceil(n)
            years = math.floor(number_of_months / 12)
            months_left = number_of_months % 12

            if months_left == 0:
                if years > 1:
                    overpayment = ((years * 12) * payment) - principal
                    print("It will take ", years, "years to repay this loan!")
                    print("Overpayment = ", overpayment)
                else:
                    print("It will take 1 year to repay the loan")
            else:
                if years > 1:
                    print("It will take ", years, "years and ", months_left, "months to repay this loan!")
                else:
                    print("It will take ", months_left, "months to repay this loan!")

    elif payment == 0:
        temp = pow((1 + nominal_interest_rate), periods)
        monthly_rate = principal * (nominal_interest_rate * temp) / (temp - 1)
        print("Yor monthly payment = ", math.ceil(monthly_rate), "!")

        overpayment = (periods * math.ceil(monthly_rate)) - principal
        print("Overpayment = ", overpayment)

else:
    print("Incorrect parameters")