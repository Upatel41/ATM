#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 17:46:03 2021

@author: umapatel
"""

import json

def readjson():
    with open('cards.json','r') as f:
        cards = json.load(f)
        f.close()

    with open('accounts.json','r') as f:
        accounts = json.load(f)
        f.close()
    return cards,accounts

def nr_of_notes(amount):
    notes = [20,10,5,2,1]
    print(f"Dispensing ${amount} as ",end='')
    l=[]
    for note in notes:
        if amount >= note:
            x = f" {int(amount/note)}x${note} "
            l.append(x)
            amount = amount - (int(amount/note)*note)
        else:
            pass
    print('+'.join(l))

def modify(account,method):
    with open('accounts.json','r') as f:
        accounts = json.load(f)
        f.close()
    if method == 'withdraw':
        balance = accounts['accounts'][account]['balance']
        print("Your Current Balance : ",balance)
        amount = int(input("Enter Amount to withdraw : ")) 
        if (balance-amount) < 0:
            print("Insufficient Balance!!!")
        else:
            c_balance = balance - amount
            accounts['accounts'][account]['balance'] = c_balance
            json_object = json.dumps(accounts, indent = 4)
            with open("accounts.json", "w") as outfile:
                outfile.write(json_object)
                outfile.close()
            print("New Balance : ",c_balance)
            nr_of_notes(amount)
            print("Thank You for choosing python bank")
    else:
        balance = accounts['accounts'][account]['balance']
        print("Your Current Balance : ",balance)
        amount = int(input("Enter Amount to deposit : "))  
        c_balance = balance + amount
        accounts['accounts'][account]['balance'] = c_balance
        json_object = json.dumps(accounts, indent = 4)
        with open("accounts.json", "w") as outfile:
            outfile.write(json_object)
            outfile.close()
        print("Balance added Successfully")
        print("New Balance : ",c_balance)
        print("Thank You for choosing python bank")

if __name__ == '__main__':
    cards,accounts = readjson()
    pin = "0"
    while(len(pin) != 4 or not pin.isdigit()):
        pin = input("Please enter your PIN number : ")
    
    info = None
    account = None
    if pin not in cards['cards']:
        print("We do not have a account associated with that PIN number. Please try again")
    else:
        for card in cards['cards']:
            if card == pin:
                info = cards['cards'][pin]
                print(f"Hello {info['name']} would you like to withdraw or deposit?")
                
                break
    if info != None:
        account = info['account']
        option = ""
        while(option != "withdraw" and option != "deposit"):
            option = input("> ")
        
            if option == "withdraw":
                modify(account,option)
                break
            elif option == "deposit":
                modify(account,option)
                break
            else:
                print("Please try again")

    
            