months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ")
    if "/" in date:
        month, day, year = date.split("/")
        try:
            month = int(month)
            day = int(day)
            if month > 12 or day > 31:
                continue
        except ValueError:
            continue
        break

    elif ',' in date:
        date = date.replace(",", "")
        month, day, year = date.split(" ")
        if month in months:
            month = months.index(month) + 1
            try:
                day = int(day)
                if month > 12 or day > 31:
                    continue
            except ValueError:
                continue
            break

print(str(year) + '-' + f"{int(month):02}" + '-' + f"{int(day):02}")

