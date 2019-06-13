"""
title: string_practice
author: Cameron
date: 2019-06-11 13:45
"""
import random

kid = input("Enter a letter: ")
print(kid.lower() in "qwertyuiopasdfghjklzxcvbnm")



short = input("Enter a text")

short = short.lower().replace("and", "&")
short = short.lower().replace("too", "2")
short = short.lower().replace("you", "^")
short = short.lower().replace("for", "4")

short = short.lower().replace("a", "")
short = short.lower().replace("e", "")
short = short.lower().replace("i", "")
short = short.lower().replace("o", "")
short = short.replace("^", "U")
print(short)


phrase = input(">>> Enter a phrase: ")
phrase = phrase.replace(" ", "").replace(",", "").replace(".", "").replace("/", "").replace(";", "").replace(":", "").replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("'", "")
print(phrase.lower())


phrase = input(">>> Enter a phrase: ")
phrase = phrase.lower().replace(" ", "").replace(",", "").replace(".", "").replace("/", "").replace(";", "").replace(":", "").replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("'", "")
print(phrase == phrase[::-1])

fname = input("Enter First Name: ")
lname = input(">>> Enter Last Name: ")
bcity = input(">>> Enter Birth City: ")
uni = input(">>> Enter Alma Mater University: ")
relative = input(">>> Enter a Relative's Name: ")
friend = input(">>> Enter a Friend's Name: ")
print("")
eid = fname[0:3] + lname[-2:]
uname = bcity[0:2] + uni[-3:]
num = len(relative)
numb = len(friend)
password = relative[(random.randint(0, num)):] + friend[0:(random.randint(0, numb))]

print(f"Employee ID: {eid}")
print(f"User Name: {uname}")
print(f"Password: {password}")



