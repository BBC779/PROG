import datetime

print("Skriv start året nu")
start_year = input()
start_year = int()

print("Skriv start månaden nu")
start_month = input()
start_month = int(start_month)

print("Skriv start dagen nu")
start_day = input()
start_day = int(start_day)

print("Skriv slut året nu")
end_year = input()
end_year = int(end_year)

print("Skriv slut månaden nu")
end_month = input()
end_month = int(end_month)

print("Skriv slut dagen nu")
end_day = input()
end_day = int(end_day)

start_date = datetime.datetime (start_year, start_month, start_day)
end_date = datetime.datetime (end_year, end_month, end_day)

date_diff = (end_date - start_date).days
print(date_diff)

meter_start = input("Skriv elmätarens startvärde:")
meter_end = input("Skriv elmätarens slutvärde:")
meter_start = int (meter_start)
meter_end = int (meter_end)

consumed = meter_end - meter_start

day_fee = input("Pris dagsavgift:")
kwh_price = input("Pris per kWh")

day_fee = int (day_fee)
kwh = float (kwh_price)

total_price = (date_diff * day_fee + consumed * kwh_price) * 1.25

print("Dett totala priset efter skatt:", total_price)