from math import ceil
from math import floor
from math import log
import sys

args = sys.argv
option = None
periods = None
payment = None
principal = None
interest = None

if len(args) != 5: 
    "quick error check"
    print("Incorrect parameters")
    exit()
else:
    "this section assigns values to relevant variable by iterating each element of args list"
    for i in range(1, 5):
        element = args[i]
        if "type" in element:
            option = element
            option = option.split("=")[1]
        if "periods" in element:
            periods = element
            periods = int(periods.split("=")[1])
        if "payment" in element:
            payment = element
            payment = int(payment.split("=")[1])
        if "principal" in element:
            principal = element
            principal = int(principal.split("=")[1])
        if "interest" in element:
            interest = element
            interest = float(interest.split("=")[1])
            interest = interest / (12 * 100)  # conversion to a monthly interest

if option == "annuity" and principal is None:
    principal = payment / ((interest * (1 + interest) ** periods)
                           / ((1 + interest) ** periods - 1))
    principal = floor(principal)
    overpayment = payment * periods - principal
    overpayment = ceil(overpayment)
    print("Your credit principal = " + str(principal) + "!")
    print("Overpayment = " + str(overpayment))

elif option == "annuity" and payment is None:
    annuity_payment = principal * (interest * (1 + interest) ** periods) \
                      / ((1 + interest) ** periods - 1)
    annuity_payment = ceil(annuity_payment)
    overpayment = annuity_payment * periods - principal
    print("Your annuity payment = " + str(annuity_payment) + "!")
    print("Overpayment = " + str(overpayment))

elif option == "annuity" and periods is None:
    x = payment / (payment - interest * principal)
    log_base = (1 + interest)
    periods = log(x, log_base)
    periods = int(ceil(periods))
    print(periods % 12)
    if periods % 12 == 0:
        print("You need " + str(periods // 12) + " years to repay this credit!")
    elif periods % 12 != 0:
        print("You need " + str(periods // 12) + " years and "
              + str(periods % 12) + " months to repay this credit!")
    else:
        print("You need " + str(periods) + " months to repay this credit!")
    overpayment = payment * periods - principal
    print("Overpayment = " + str(overpayment))

elif option == "diff":
    if interest is None:
        print("Incorrect parameters")
        exit()
    total_paid = 0
    for month in range(1, periods + 1):
        differentiated_payment = (principal / periods) + interest * (
                principal - (principal * (month - 1)) / periods)
        differentiated_payment = ceil(differentiated_payment)
        total_paid += differentiated_payment
        print("Month " + str(month) + ": paid out " + str(differentiated_payment))
    overpayment = total_paid - principal
    print()
    print("Overpayment = " + str(overpayment))