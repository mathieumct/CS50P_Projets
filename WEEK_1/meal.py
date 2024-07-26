def main():
    t = (input("What time is it ? "))
    t=convert(t)

    if t >= 7 and t <= 8:
        print("breakfast Time")
    elif t >= 12 and t <= 13:
        print("lunch Time")
    elif t >= 18 and t <= 19 :
        print("dinner Time")


def convert(time):
    hours, minutes = time.split(":")
    time = (float(hours) + float(minutes)/60)
    return time

if __name__ == "__main__":
    main()