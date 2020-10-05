import math #not necessary but out of respect for Fermat and his successors, I include the math module.
def check_Fermat(a,b,c,n):
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int) and isinstance(n, int): #first check that all attributes are integers
        if n>2 and (a**n)+(b**n)==(c**n):           #I love math.
            print('Holy smokes, Fermat was wrong!') #Sir Wiles would roll out of his bed in dispair if someone entered a combination of numbers that resulted in this output.
        elif n<=2:
            print("Well that's not what the theorem was claiming...") #using a double quote to allow a single quote in the string
        elif n>2 and (a**n)+(b**n)!=(c**n):
            print("No, that doesn't work.") #using a double quote to allow a single quote in the string
    else: #Just in case someone enters anything besides integers
        print('You entered something that does not make sense. Make sure all attributes of function are integers.')
       
       

