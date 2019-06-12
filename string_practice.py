"""
title: string_practice
author: Cameron
date: 2019-06-11 13:45
"""
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


hrase = input(">>> Enter a phrase: ")
phrase = phrase.replace(" ", "").replace(",", "").replace(".", "").replace("/", "").replace(";", "").replace(":", "").replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("'", "")

