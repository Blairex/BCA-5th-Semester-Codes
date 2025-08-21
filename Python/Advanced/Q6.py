# 6. Write a program that takes user input for a day and checks if it's a weekday using a tuple.
weekdays = ("monday", "tuesday", "wednesday", "thursday", "friday")

day = input("Enter a day: ").lower()
if day in weekdays:
    print(day, "is a weekday")
else:
    print(day, "is not a weekday")
# Added extra info
