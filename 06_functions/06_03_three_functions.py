'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
def days_to_hours(days):
    return days * 24

def hours_to_minutes(hours):
    return hours * 60

def days_to_minutes(days):
    hours = days_to_hours(days)
    minutes = hours_to_minutes(hours)
    return minutes

d = int(input("enter number: "))
m = days_to_minutes(d)

print(d,"days are", m, "Minutes")