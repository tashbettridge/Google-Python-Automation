#!/usr/bin/env python
# coding: utf-8

# Which of the following scenarios would benefit the most from using a recursive function to solve the problem?
# 
# You need to create a family tree, showing several generations of your ancestors, with all of their children. (You're getting the concept of recursion and when it's a better solution than the traditional looping techniques.)

# Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. Note: base is assumed to be a positive number. Tip: for functions that return a boolean value, you can return the result of a comparison.

# def is_power_of(number, base):# Base case: when number is smaller than base.
#     if number ==1:
#         return True
#     if number < base:# If number is equal to 1, it's a power (base**0).
#         return False 
# number /= base
# #Recursive case: keep dividing number by base.
# 
# return is_power_of(number, base)
# print(is_power_of(8,2)) # Should be True
# print(is_power_of(64,4)) # Should be True
# print(is_power_of(70,10)) # Should be False

# Fill in the blanks of this code to print out the numbers 1 through 7.

# In[1]:


number = 1
while number in range (1,8):
    print(number, end=" ")
    number +=1


# The show_letters function should print out each letter of a word on a separate line. Fill in the blanks to make that happen.

# In[2]:


def show_letters(word):
    for letter in word:
        print(letter)
show_letters("Hello")


# Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits. Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.

# In[3]:


def digits(n):
    count = 0
    if n == 0:
      return 1 
    while (n > 0):
        count += 1
        n = n//10
    return count
    
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits. Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.
# In[5]:


def multiplication_table(start, stop):
    for x in range (start,stop+1):
        for y in range(start,stop+1):
            print(str(x*y), end=" ")
        print()

multiplication_table(1, 3)
# Should print the multiplication table shown above


# The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. Fill in the blanks to make this work correctly.

# What is the value of x at the end of the following code?
# for x in range(1, 10, 3):
# print(x)

# In[6]:


for x in range(1, 10, 3):
    print(x)


# What is the value of y at the end of the following code? #8
# 

# In[8]:


for x in range(10):
    for y in range(x):
        print(y)

