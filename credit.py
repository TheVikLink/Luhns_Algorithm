# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 08:56:09 2021

@author: feolvi
"""

import math

def luhns_algorithm(num):
    
    number = num #from this number we will get every other digit
    number2 = num #from this number we will get the other digits not included in every other digit
    every_other_digit = [] #we will append every other digit to this list
    not_every_other_digit = [] #we will append the other digits to this list
    every_other_digit_times_two = [] #we will append every other digit multiplied by two to this list
    sum_of_digits_every_other_digit_times_two = 0 #Counter to store the sum of the digits of the numbers in the list 
                                                  #every_other_digit_times_two
    valid = False #The default is that the credit card is not valid. If the last digit of the target sum is 0, the card is valid
    
    #In the following two while loops, the goal is to split the digits of num in two halves and store those halves in two separate lists
    
    while number > 1: #We will divide the number until it is less than zero, which means there are no more digits
        number /= 10 #Get rid of the last digit
        rem = number % 10 #Get the last digit
        every_other_digit.append(rem) #Append the last digit to list
        number /= 10 #Get rid of the last digit and repeat
    
    while number2 > 1: #Same as above, but this time we will get the other half of the digits
        rem = number % 10 #Get the last digit
        not_every_other_digit.append(rem) #Append the last digit to list
        number /= 100 #Get rid of the last two digits
    
    #In this for loop we iterate through the digits in every_other_digits and appends those digits multiplied by two to a new list
    for digit in every_other_digit: #
        every_other_digit_times_two.append(digit * 2)
    
    #Because we are supposed to add only the digits of the products of every other digit times two, we must create
    #two conditionals. The first if- statement is for digits from 0-9. The else- statement is for numbers > 10, 
    #where we must first split the two digits and then sum those digits to sum_of_digits_every_other_digit_times_two
    
    for digit in every_other_digit_times_two:
        if digit < 10:
            sum_of_digits_every_other_digit_times_two += digit
    
        else:
            second_digit = digit % 10 
            first_digit = math.floor(digit / 10)
            sum_of_digits_every_other_digit_times_two += first_digit
            sum_of_digits_every_other_digit_times_two += second_digit
    
    #Creates empty counter so that we can add the digits not multiplied by two
    sum_of_digits_not_multiplied_by_two = 0
    
    #Iterates through digits in the half that is not multiplied by two, and adds them to counter
    
    for digit in not_every_other_digit:
        sum_of_digits_not_multiplied_by_two += digit
    
    #Finally we can get the target sum, which is the sum of the two counters we have made above
    
    target_sum = sum_of_digits_every_other_digit_times_two + sum_of_digits_not_multiplied_by_two
    
    #If last digit of target sum is 0, the credit card number is legit
    
    if target_sum % 10 == 0:
        valid == True
    
    return valid
        
#In this function we will determine which company has issued the credit card, and use our function luhns_algorithm to
#check if the credit card number is valid
    
def credit_card(num):
    
    digits = 0
    company = ""
    
    valid = luhns_algorithm(num)
    
    if valid = True:
    
        for digit in num:
            digits += 1
        
        first_two_digits = num / 10 ** (digits - 2)
        first_two_digits = math.floor(first_two_digits)
        first_digit = first_two_digits / 10
            
        if digits == 15:
            if first_two_digits == 34 or first_two_digits == 37:
                company = "AMEX"
        
        elif digits == 13:
            company = "VISA"
        
        elif digits == 16 and first_digit == 4:
            company = "VISA"
        
        elif digits == 16 and 51 <= first_two_digits <= 55:
            company = "MasterCard"
        
        return print("The credit card is issued by " + company)
    
    else:
        
        return print("The credit card number is invalid.")
    
    