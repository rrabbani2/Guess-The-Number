import random

def number_checker(number):
    guesser = random.randint(1,10)
    if int(number) ==  guesser:
        return {"win":True,"answer":guesser}
    else:
        return {"win":False,"answer":guesser}
       
