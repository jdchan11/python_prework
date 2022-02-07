#Question 1
def hello_name(user_name):
    """Prints a simple message 'hello_USERNAME!'"""
    print("hello_" + user_name.upper() + "!")

#Question 2
def first_odds():
    """Prints the odd numbers from 1 to 100 but returns nothing"""
    odds = list(range(1,100,2))
    print()


first_odds()

#Question 3
def max_num_in_list(a_list):
    """Returns the max number of a given list"""
    a_list = [my_list]
    print(max(my_list))

my_list = [1, 23, 64, 35, 86, 57, 99, 2]
max_num_in_list(my_list)

#Question 4:
def is_leap_year(a_year):
    """Will return true or false depending on if the given year is a leap year"""
    
    if a_year % 4 == 0 and a_year % 100 > 0:
        return True
    elif a_year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(2024))

#Question 5: 
def is_consecutive(a_list):
    """Check to see if all numbers in a list are consecutive."""
    sorted_list = sorted(a_list)
    constant_list = list(range(min(a_list), max(a_list) + 1))
    if sorted_list == constant_list:
        return True
    else:
        return False
a_list = [2, 4, 3, 5, 1]
print(is_consecutive(a_list))

