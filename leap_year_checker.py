# Leap year calculation
# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# The year is a leap year (it has 366 days).
# The year is not a leap year (it has 365 days).

def is_it_a_leap_year():
    year = int(input("Enter any year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("It's a leap year.")
            else:
                print("It's not a leap year.")
        else:
            print("It's a leap year.")
    else:
        print("It's not a leap year.")


is_it_a_leap_year()
