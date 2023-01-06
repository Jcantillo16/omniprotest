import datetime


def get_date(date_str):
    date = datetime.datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S %z")
    return date


def get_days(date1, date2):
    days = []
    for i in range((date2 - date1).days + 1):
        day = date1 + datetime.timedelta(days=i)
        days.append(day.strftime("%A"))
    return days


def get_hours(date1, date2):
    hours = 0
    for i in range((date2 - date1).days + 1):
        day = date1 + datetime.timedelta(days=i)
        if day.weekday() < 5:
            hours += 8
    return hours


def get_diff(date1, date2):
    diff = date2 - date1
    return diff.total_seconds(), diff.total_seconds() / 3600, diff.days


def get_diff_tz(date1, date2):
    diff = date2.astimezone(date1.tzinfo) - date1
    return diff.total_seconds(), diff.total_seconds() / 3600, diff.days


def main():
    date1 = get_date("01/01/2020 00:00:00 +0000")
    date2 = get_date("31/12/2020 23:59:59 +0000")
    days = get_days(date1, date2)
    print("Days between dates:")
    for day in set(days):
        print(f"{day}: {days.count(day)}")
    print(f"Hours between dates: {get_hours(date1, date2)}")
    print("Difference between dates:")
    print(f"Seconds: {get_diff(date1, date2)[0]}")
    print(f"Hours: {get_diff(date1, date2)[1]}")
    print(f"Days: {get_diff(date1, date2)[2]}")
    date1 = get_date("01/01/2020 00:00:00 -0500")
    date2 = get_date("31/12/2020 23:59:59 +0000")
    print("Difference between dates (different timezones):")
    print(f"Seconds: {get_diff_tz(date1, date2)[0]}")
    print(f"Hours: {get_diff_tz(date1, date2)[1]}")
    print(f"Days: {get_diff_tz(date1, date2)[2]}")


if __name__ == "__main__":
    main()
