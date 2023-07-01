income = [10, 30, 75]

def double_money(dollars):
    return 2*dollars

new_income = list(map(double_money, income))
print(new_income)

"""equals to the down below but easier
for item in income.items():
    double_money(item) ... and so on
"""