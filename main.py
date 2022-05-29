from datetime import datetime
import enums


def is_max_day_reached(month_name, days):
    max_day = enums.MonthsLastDay.months_dict[month_name]
    if max_day > days:
        return True
    return False


def is_leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False


def add_days_to_current_date(starting_date, add_days=1):
    # DD-MM-YYYY
    splitten_date = starting_date.split("-")
    day, month, year = [int(x) for x in splitten_date]
    _is_leap_year = is_leap_year(year)
    _days_counter = add_days
    _month_to_add = 0

    for month_item in enumerate(enums.MonthsLastDay.months_dict):
        if month == (month_item[0] + 1):
            current_month_max = enums.MonthsLastDay.months_dict[month_item[0+1]]
            if current_month_max < _days_counter and _days_counter == 0:

                _days_counter = current_month_max - _days_counter
                _month_to_add += 1
            elif enums.General.MINIMUM_DAY < _days_counter > 0:
                day += _days_counter

    if _month_to_add > 0 and (month + _month_to_add) > enums.General.MAXIMUM_MONTHS:
        year += 1

    print(datetime(year, month, day))
    return


if __name__ == '__main__':
    add_days_to_current_date("15-05-1988", 50)
    # result = days_to_months_converter('MAY', 32)
