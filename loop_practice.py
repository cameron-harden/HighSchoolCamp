"""
title: loop_practice
author: Cameron
date: 2019-06-13 13:38
"""
nums = [89, 41, 73, 90]
for i in nums:
    print(i)

for i in range(5,15):
    print(i)

for i in range(100, 201, 10):
    print(i)

for i in range(80, 31, -8):
    print(i)

for i in range(3):
    print("Alright")

intt = 10
while intt > 0:
    print(intt)
    intt = intt- 15

num = int(input("Enter an integer that is greater than 0.  "))


while num < 0:
    num = int(input("Enter an integer that is greater than 0.  "))


num1 = int(input("Enter an number that will be smaller than the next.  "))
num2 =int(input("Enter the second, greater number.  "))

while num1>num2:
    print("Invalid response")
    num1 = int(input("Enter an number that will be smaller than the next.  "))
    num2 = int(input("Enter the second, greater number.  "))

while num1 < num2 + 1:
    print(num1)
    num1 = int(num1 + 1)

speak = input("respond by 'Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO'.")
while speak not in ['Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO']:
    speak = input("respond by 'Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO'.")

