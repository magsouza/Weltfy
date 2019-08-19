import datetime
from date_handler import get_3weeks
from csv_gen import generate_csv, filter_csv

country = input("Enter the country you want a playlist from: ")
today = datetime.date.today()
weeks = get_3weeks()
csv = generate_csv(weeks, country)
filtered = filter_csv(csv, country)
print(filtered)