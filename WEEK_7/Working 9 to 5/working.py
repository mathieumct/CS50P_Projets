import re


def main():
    s = input("Hours: ").strip()
    hour_converted = convert(s)
    print(f"{hour_converted[0][0]:02d}:{hour_converted[0][1]:02d} to {hour_converted[1][0]:02d}:{hour_converted[1][1]:02d}")



def convert(s):
    match = re.search(r"(\d{1,2}):(\d{1,2}) (AM|PM) to (\d{1,2}):(\d{1,2}) (AM|PM)", s)
    if not match:
        match = re.search(r"(\d{1,2}) (AM|PM) to (\d{1,2}) (AM|PM)", s)
    if match == None:
        raise ValueError("Invalid Format")
    if len(match.groups()) == 4:
        hour1, am_pm1, hour2, am_pm2 = match.groups()
        minute1 = 0
        minute2 = 0
        hour1 = int(hour1)
        hour2 = int(hour2)
    else:
        hour1, minute1, am_pm1, hour2, minute2, am_pm2 = match.groups()
        hour1 = int(hour1)
        minute1 = int(minute1)
        hour2 = int(hour2)
        minute2 = int(minute2)
    if not (0 <= hour1 < 24 and 0 <= minute1 < 60):
        raise ValueError("Invalid Time")
    if not (0 <= hour2 < 24 and 0 <= minute2 < 60):
        raise ValueError("Invalid Time")

    if hour1 == 12 and am_pm1 == "AM":
        hour1 = 0
    elif hour1 == 12 and am_pm1 == "PM":
        hour1 = 12
    elif 1 <= hour1 < 12 and am_pm1 == "PM":
        hour1 += 12

    if hour2 == 12 and am_pm2 == "AM":
        hour2 = 0
    elif hour2 == 12 and am_pm2 == "PM":
        hour2 = 12
    elif 1 <= hour2 < 12 and am_pm2 == "PM":
            hour2 += 12
    return (hour1, minute1), (hour2, minute2)

if __name__ == "__main__":
    main()
