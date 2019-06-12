"""
title: random_salary
author: Cameron
date: 2019-06-12 09:52
"""
import random

name = input("Enter your name")
salary = int(input(">>> Enter your salary"))
raise_per = random.randint(0,100)
raise_amount = salary + ((salary / 100) * raise_per)

print(str(name) + " your current salary is $" + str(salary) + ".")
print("Your raise is " + str(raise_per) + "% of $" + str(salary) + ".")
print(str(name) + ", your new salary is " + str(raise_amount))
