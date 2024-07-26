while True:
    try:
        date = input("Date: ")
        date = date.replace(" ", "")
        months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
            ]


        from datetime import datetime
        if "/" in date:
            convert_date = datetime.strptime(date, "%m/%d/%Y")
            date_only = convert_date.date()
            print(date_only)
            break
        elif "," in date:
            month_day_year = date.split(",")
            year = month_day_year[1]
            month_day = month_day_year[0][:-1]
            day = month_day_year[0][-1]
            new_date = month_day + " " + day
            day = int(day)
            if day > 31:
                break
            month_number = str(months.index(month_day) + 1).zfill(2)
            result_date = "-".join([str(year), str(month_number), str(day).zfill(2)])
            result_date = result_date.replace(" ", "")
            print(result_date)
            break
    except:
        continue
