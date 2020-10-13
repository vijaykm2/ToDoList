def final_deposit_amount(*interests, amount=1000):
    result = amount
    for interest in interests:
        result *= (1+interest/100)
    return round(result, 2)

 # print(final_deposit_amount(5,7,4))