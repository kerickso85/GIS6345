import math #not necessary but out of respect for Fermat and his successors, I include the math module.
def check_Fermat():
    def theorem_test(int_a,int_b,int_c,exponent_n):
        if exponent_n>2 and (int_a**exponent_n)+(int_b**exponent_n)==(int_c**exponent_n): 
            print('Holy smokes, Fermat was wrong!') #Sir Wiles would roll out of his bed in dispair if someone entered a combination of numbers that resulted in this output.
        elif exponent_n<=2:
            print("Well that's not what the theorem was claiming...") #using a double quote to allow a single quote in the string
        elif exponent_n>2 and (int_a**exponent_n)+(int_b**exponent_n)!=(int_c**exponent_n): 
            print("Sorry, that combination doesn't work.") #using a double quote to allow a single quote in the string
        else:
            print('Something went horribly wrong here...')

    print("Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.")
    a=input('Enter a value for "a":')
    try:
        int_a = int(a) #test if the value of a is an integer type
        #print('a=',int_a)
    except ValueError:
        try:
            float_a = float(a) #test if the value of a is an float type and if not, convert it to an integer
            int_a = int(float_a)
            #print('a=',int_a)
        except ValueError:
            int_a = a #if not an integer or float, ensure something is passed forward so it re-executes
            print('You need to input only numbers if you want this to work...')

    b=input('Enter a value for "b":')
    try:
        int_b = int(b) #test if the value of b is an integer type
        #print('b=',int_b)
    except ValueError:
        try:
            float_b = float(b) #test if the value of b is an float type and if not, convert it to an integer
            int_b = int(float_b)
            #print('b=',int_b)
        except ValueError:
            int_b = b #if not an integer or float, ensure something is passed forward so it re-executes
            print('You need to input only numbers if you want this to work...')

    c=input('Enter a value for "c":')
    try:
        int_c = int(c) #test if the value of c is an integer type
        #print('c=',int_c)
    except ValueError:
        try:
            float_c = float(c) #test if the value of c is an float type and if not, convert it to an integer
            int_c = int(float_c)
            #print('c=',int_c)
        except ValueError:
            int_c = c #if not an integer or float, ensure something is passed forward so it re-executes
            print('You need to input only numbers if you want this to work...')

    n=input('Enter a value for "n":')
    try:
        exponent_n = int(n) #test if the value of n is an integer type
        #print('n=',exponent_n)
    except ValueError:
        try:
            exponent_n = float(n) #test if the value of n is an float type and if not, convert it to an appopriate integer value.
            if 3>exponent_n>2:
                exponent_n=int(exponent_n)+1 #I made a conscious decision to round anything greater than 2 but less than 3 up to the next integer. All others floats are truncated as usual.
                print('n has been rounded to',exponent_n)   #It didn't seem right to be ignoring exponents such as 2.000001 because they were being truncated to 2 and causing a "Well that's not what the theorem was claiming..." response.
            else:
                exponent_n=int(exponent_n)
                print('n has been rounded to',exponent_n)
        except ValueError:
            exponent_n = n #if not an integer or float, ensure something is passed forward so it re-executes
            print('You need to input only numbers if you want this to work...')
    
    if isinstance(int_a, int) and isinstance(int_b, int) and isinstance(int_c, int) and (isinstance(exponent_n,int) or isinstance(exponent_n,float)):
        theorem_test(int_a,int_b,int_c,exponent_n) #sends off the user input values to the sub function that calculates if the equation is satisfied.
    else:
        print('Sorry, one of your values was not a number. Please try again.') #if one input wasn't a number, it restarts the __main__ function
        check_Fermat()
    

    


     
       
       

