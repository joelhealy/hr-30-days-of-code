actual_date = input().split()
expected_date = input().split()
day_actual = int(actual_date[0])
day_expected = int(expected_date[0])
month_actual = int(actual_date[1])
month_expected = int(expected_date[1])
year_actual = int(actual_date[2])
year_expected = int(expected_date[2])
# print("Actual Date(D-M-Y): {}-{}-{}".format(day_actual, month_actual, year_actual))
# print("Expected Date(D-M-Y): {}-{}-{}".format(day_expected, month_expected, year_expected))

if year_expected == year_actual:
    if month_expected == month_actual:
        if day_expected < day_actual:
            print(15*(day_actual - day_expected))
        else:
            print(0)
    elif month_expected < month_actual:
        print(500*(month_actual - month_expected))
    else:
        print(0)
elif year_expected < year_actual:
    print(10000)
else:
    print(0)

