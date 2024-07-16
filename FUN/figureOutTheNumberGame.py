import random 
import sys
lists = ["1" , "2" , "3", "4", "5", "6" , "7", "8", "9"]
number = ""
def generateNumber ():
    global number
    for i in range(4):
        rand_number = random.choice(lists)
        lists.remove(rand_number)
        number += rand_number

generateNumber()

def check(num):
    cnum = 0
    pos = 0
    if num == number:
        print("Cogradulation you have Found the number!!!")
        sys.exit()
    for i in range(4):
        if number.find(num[i]) != -1:
            cnum += 1
            if number.index(num[i]) == num.index(num[i]):
                pos += 1
    print ("Correct Numbers " + str(cnum))
    print ("Correct Positions " + str(pos))
    

print("\n"+ " Guess The Number ".center(50 , "-") + "\n")

for i in range(10): 
    print ("Guess the four digit Number:" , end=" ")
    guess = input()
    if guess.isnumeric():
        check(guess)
    else: print("Enter a Valid Number!")

print ("GAME OVER!!!")
print ("The Number Was " + number)



# GAME RULES 

""" 
A 4 digit Number is generated with unique digits and excluding zero ( for Example: Valid Numbers: 3478 , 9836
Invalid Numbers: 3538 , 6480 ... )

You are given ten chances to figure out the Number with a sequence of tries. each time you are given the number of correct digits u have guessed and the number of correct positions they are in. 

Example: If the Number Generated is 8256 and you guessed 1659 
Correct Numbers = 2 , since 5 and 6 are correct )  
Correct Positions = 1 , since only 5 is in the correct posstion(third) )

With the given hints You are expected to get the correct 4 digit Number before 10 tries. 

"""

# Note: in the future, i will add different validations , error handlings and GUI for better Experience 