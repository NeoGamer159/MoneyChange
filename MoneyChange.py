# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 11:58:20 2024

@author: cernym
"""

money_to_change = 120563

change_money = [5000,2000,500,200,100,50,20,10,5,2,1]

def calculate_change(money_to_change, change_money):
    result = {}
    for bill in change_money:
        count = money_to_change // bill
        if count:
            result[bill] = count
            money_to_change -= bill * count
    return result

change = calculate_change(money_to_change, change_money)
print(change)

