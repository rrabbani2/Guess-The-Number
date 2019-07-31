import random

#Our number guesser
# numbers = [1,2,3,4,5,6,7,8,9,10]

# guesser =(str(numbers[random.randint(0,len(numbers)-1)]))
guesser = random.randint(1,10)
for i in range(20):
    print(random.randint(1,10))


def number_checker():
    x = 5
    while x>0:
        number = input("I am thinking of a number from 1 to 10. What would you like to guess?")
        if int(number) ==  guesser:
            print("Good job, you guessed my number!")
            return
        else:
            x=x-1
            print("Not quite try again")
            print("You have "+ str(x)+ " chances left")
            if int(number) <  guesser:
                print("Hint:Try a number a little HIGHER")
            elif int(number) > guesser:
                print("Hint:Try a number a little LOWER")
            if int(number) > 10:
                 print("PLEASE CHOOSE A NUMBER FROM 1 TO 10")
            elif int(number) < 1:
                print("PLEASE CHOOSE A NUMBER FROM 1 TO 10")
           
       
    



number_checker()
