import datetime

name = input("Enter your name:\n")

last_name = input("Enter your last name:\n")

born = input("When were you born?\n")

city = input("Where are you from?\n")

while True:

    present_time = datetime.date(2023, 2, 3).year

    born = datetime.date(int(born), 1, 1).year

    date_str = present_time - born

    if born > 2023:
        print("Неверный год рождения, попробуйте ввести снова")
        born = input("When were you born?\n")
    else:
        print(f" {name.capitalize()} {last_name.capitalize()}. You are {date_str} years old. You are living in {city.capitalize()}.")
        break




