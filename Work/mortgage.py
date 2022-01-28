# mortgage.py
#
# Exercise 1.7

from calendar import month


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
months = 0

while principal > 0:
    months += 1
    if extra_payment_start_month <= months <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:
        # last payment is less than usual:
        if principal * (1+rate/12) < payment:
            last_payment = principal * (1+rate/12)
            principal = principal * (1+rate/12) - last_payment
            total_paid = total_paid + last_payment
        else:
            principal = principal * (1+rate/12) - payment
            total_paid = total_paid + payment
    print(f'Month: {months}, paid: {total_paid:,.2f} principal: {principal:>10,.2f}')

print('Total paid:', '{:,.2f}'.format(total_paid))
print(f'Mortgage paid in {months} months')