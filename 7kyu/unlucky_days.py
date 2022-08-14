import calendar


def unlucky_days(year):
    cal = calendar.Calendar()
    count = 0
    for m in range(1, 13):
        for numer, numer_day in cal.itermonthdays2(year, m):
            if numer == 13 and numer_day == 4:
                count +=1
    return count

print(unlucky_days(2015))

