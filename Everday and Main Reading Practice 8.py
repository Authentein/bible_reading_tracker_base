from datetime import date

today = date.today()

day_of_the_year = today.timetuple().tm_yday

day = today.day

if day <= 14:
    main_reading = "1 Kings"

else:
    main_reading = "1 Chron"

psalms = (day - 1) % 150 + 1

proverbs = (day - 1) % 31 + 1

print(f"Day of the year: {day_of_the_year}")
print(f"Read: {main_reading}, Psalms {psalms}, Proverbs {proverbs}")

