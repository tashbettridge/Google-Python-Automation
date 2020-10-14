#!/usr/bin/env python
# coding: utf-8

# # Hello World!

# Replace the ___ placeholder and calculate the Golden ratio: \frac{1+\sqrt{5}}{2}21+5​​.
# Tip: to calculate the square root of a number xx, you can use x**(1/2).

# In[1]:


ratio = (1 + 5 ** 0.5) / 2
print(ratio)


# # Expressions, Numbers and Type Conversions

# In this scenario, we have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8. Fill in the blanks to calculate the average file size by having Python add all the values for you, and then set the files variable to the number of files. Finally, output a message saying "The average size is: " followed by the resulting number. Remember to use the str() function to convert the number into a string.

# In[2]:


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


# In[7]:


def rectangle_area(base, height):
    area = base * height
    return area    
print("The area is ", rectangle_area(5,6))


# In[8]:


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

# In[9]:


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

# In[10]:


def lucky_number(name):
    number = len(name) * 9
    return "Hello " + name + ". Your lucky number is " + str(number)

print(lucky_number("Kay"))
print(lucky_number("Cameron"))


# The number_group function should return "Positive" if the number received is positive, "Negative" if it's negative, and "Zero" if it's 0. Can you fill in the gaps to make that happen?

# In[11]:


def number_group(number):
    if number > 0:
        return "Positive"
    elif number == 0:
        return "Zero"
    else:
        return "Negative"
print(number_group(10))
print(number_group(0))
print(number_group(-5))


# Complete the function by filling in the missing parts. The color_translator function receives the name of a color, then prints its hexadecimal value. Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.

# In[12]:


def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown


# Question 4
# Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score". Fill in this function so that it returns the proper grade.

# In[13]:


def exam_grade(score):
	if score == 100:
		grade = "Top Score"
	elif 95 >= score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail


# If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?

# In[14]:


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize//4096
        # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize%4096
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return 4096*(full_blocks+1)
    return(calculate_storage(1))

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


# In[ ]:




