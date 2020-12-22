import calendar

def splittedDate(items):
    items = date.split("-")
    processedItems = []
    for item in items:
        processedItems.append(int(item))

    return processedItems


date = ""
while True:
    try:
        date = input("Enter date in format: dd.mm.yyyy (01-11-2005): ")
        date = splittedDate(date)
        assert len(date) == 3
        assert date[0] > 0 and date[0] < 32
        assert date[1] > 0 and date[1] < 13
        assert date[2] > 1970 and date[2] < 2100
        break

    except:
        print("Please enter correct date")

print("hello")

monts_info = calendar.monthrange(date[2], date[1])
days_count = monts_info[1]
print(days_count)

monthName = calendar.month_name[date[1]]
print(calendar.month_name)

print("{} {} has {} days".format(monthName, date[2], days_count))

dayNumber = calendar.weekday(date[2], date[1], date[0])
print(dayNumber)

if dayNumber in (5,6):
    print("{}-{}-{} Weekend".format(date[2], date[1], date[0]))
else:
    print("{}-{}-{} Non-Weekend".format(date[2], date[1], date[0]))