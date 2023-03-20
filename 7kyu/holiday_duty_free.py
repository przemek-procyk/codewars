def duty_free(price, discount, holiday_cost):
    savings = price * (discount * 0.01)
    return int(holiday_cost / savings)


print(duty_free(10, 10, 500))
