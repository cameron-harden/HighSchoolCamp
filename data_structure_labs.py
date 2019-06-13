"""
title: data_structure_labs
author: Cameron
date: 2019-06-13 11:33
"""
import random

def shake_ball():
    ans_list = ["Yes definitely", "As I see it, yes","Ask again later", "Cannot predict now", "Don't count on it", "Very doubtful", "Fat chance, loser", "Of course", "Never in a million years", "I don't see a reason why not"]
    num = len(ans_list) - 1
    input("Ask a question: ")
    return ans_list[random.randint(0, num)]

print(shake_ball())


def shake_ball2():
    input("Ask a question: ")
    return random.choice(["Yes definitely", "As I see it, yes", "Ask again later", "Cannot predict now", "Don't count on it","Very doubtful", "Fat chance, loser", "Of course", "Never in a million years","I don't see a reason why not"])
print(shake_ball2())

