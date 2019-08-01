import random

def number_checker(userguess):
    realnumber = random.randint(1,10)
    if int(userguess) ==  realnumber:
        return {"win":True,"answer":realnumber,"hint":"Nothing here"}
    elif int(userguess)>int(realnumber):
        return {"win":False,"answer":realnumber, "hint":"Try a lower number"}
    else:
        return {"win":False,"answer":realnumber, "hint":"Try a higher number"}

    
       
def repeatcheck(userguess, realnumber): 
    if int(userguess)==int(realnumber):
        return {"win":True,"answer":realnumber}
    elif int(userguess)>int(realnumber):
         return {"win":False,"answer":realnumber, "hint":"Try a lower number"}
    else:
        return {"win":False,"answer":realnumber,"hint":"Try a higher number"}

