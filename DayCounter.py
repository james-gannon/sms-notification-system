from datetime import date
from pickletools import uint8
from xml.etree.ElementTree import tostring

lastDate = date(2022, 9, 10)


def check_date():
    global lastDate
    print("Last date on record: " + str(lastDate))

    today = date.today()
    delta = today-lastDate
    # print(delta)
    print("Days since last date: " + str(delta.days))

    if delta.days == 28:
        print("28 days have passed!")
        lastDate = today
    else:
        print("Not yet")

    print("Final date on record: " + str(lastDate))

# check_date()
