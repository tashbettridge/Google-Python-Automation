#!/usr/bin/env python
# coding: utf-8

# # Hello World!

# Replace the ___ placeholder and calculate the Golden ratio: \frac{1+\sqrt{5}}{2}21+5​​.
# Tip: to calculate the square root of a number xx, you can use x**(1/2).

# In[2]:


ratio = (1 + 5 ** 0.5) / 2
print(ratio)


# # Expressions, Numbers and Type Conversions

# In this scenario, we have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8. Fill in the blanks to calculate the average file size by having Python add all the values for you, and then set the files variable to the number of files. Finally, output a message saying "The average size is: " followed by the resulting number. Remember to use the str() function to convert the number into a string.

# In[1]:


total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is: " + str(average))


# Combine the variables to display the sentence "How do you like Python so far?"

# In[3]:


word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"
print(str(word1) + " " + str(word2) + " " + str(word3) + " " + str(word4) + " " + str(word5) + " " + str(word6) + " " + str(word7))


# This code is supposed to display "2 + 2 = 4" on the screen, but there is an error. Find the error in the code and fix it, so that the output is correct.

# In[4]:


a = 2
b = a+a
print("2 + 2 = " + str(b) )


# Do you think you can flesh out your own function? I think you can! Let’s give it a go.
# Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours, minutes,
# and seconds function parameters.
# Remember that there are 3600 seconds in an hour and 60 seconds in a minute.

# In[5]:


def print_seconds(hours, minutes, seconds):
    print((hours*3600)+minutes*60+seconds)

print_seconds(1,2,3)


# In this code, identify the repeated pattern and replace it with a function called month_days, that receives the name of the month and the number of days in that month as parameters. Adapt the rest of the code so that the result is the same. Confirm your results by making a function call with the correct parameters for both months listed.
# 
# ### REPLACE THIS STARTER CODE WITH YOUR FUNCTION
# june_days = 30
# print("June has " + str(june_days) + " days.")
# july_days = 31
# print("July has " + str(july_days) + " days.")

# In[6]:


def month_days(month,days):
    print(month + "has " + str(days) + " days ")
month_days("June ", 30)
month_days("July ", 31)


# In[13]:


def rectangle_area(base, height):
    area = base * height
    return area    
print("The area is ", rectangle_area(5,6))


# In[18]:


def convert_distance(miles):
    km = miles * 1.6 # approximately 1.6 km in 1 mile
    return km
my_trip_miles = convert_distance(55)
# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = my_trip_miles
# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))
# 4) Calculate the round-trip in kilometers by doubling the result,
# and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_miles* 2))


# This function compares two numbers and returns them in increasing order.
# Fill in the blanks, so the print statement displays the result of the function call in order.
# Hint: if a function returns multiple values, don't forget to store these values in multiple variables

# In[22]:


# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1
# 1) Fill in the blanks so the print statement displays the result
# of the function call
(smaller, bigger)= order_numbers(100, 99)
print(smaller, bigger)


# Let's revisit our lucky_number function. We want to change it, so that instead of printing the message, it returns the message. This way, the calling line can print the message, or do something else with it if needed. Fill in the blanks to complete the code to make it work.

# In[25]:


def lucky_number(name):
    number = len(name) * 9
    return "Hello " + name + ". Your lucky number is " + str(number)
___

print(lucky_number("Kay"))
print(lucky_number("Cameron"))

