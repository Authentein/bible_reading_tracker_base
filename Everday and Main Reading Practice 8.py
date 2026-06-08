from datetime import date

# define today
today = date.today()

# define day of the year (1-365)
day_of_the_year = today.timetuple().tm_yday

# define 'day' as being today
day = today.day

# if/else defining first half and second half of the month
if day <= 14:
    main_reading = "1 Kings"

else:
    main_reading = "1 Chron"

# establish madulo for psalms/proverbs for the day within the month. Recycles when it reaches top threshold.
psalms = (day - 1) % 150 + 1

proverbs = (day - 1) % 31 + 1

# print the results, all f str.
print(f"Day of the year: {day_of_the_year}")
print(f"Read: {main_reading}, Psalms {psalms}, Proverbs {proverbs}")

