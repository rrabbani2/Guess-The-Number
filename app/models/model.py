import random

def number_checker(userguess):
    realnumber = random.randint(1,10)
    if int(userguess) ==  realnumber:
        return {"win":True,"answer":realnumber}
    else:
        return {"win":False,"answer":realnumber}
       
def repeatcheck(userguess, realnumber): 
    if userguess==realnumber:
        return {"win":True,"answer":realnumber}
    else:
        return {"win":False,"answer":realnumber}