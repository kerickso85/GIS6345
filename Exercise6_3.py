def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome():
    print("Please enter a single word to determine if it is a palindrome:")
    word=input('>>>')
    length=len(word) #find number of characters in the word
    print('Number of characters in the word are: ',length)

    if length == 1:
        print('Yes, your single character is technically a palindrome. But a lame one at that...')
    elif first(word) != last(word): #compare the first and last letter
        print("You don't have a palindrome.")
    elif first(word) == last(word):
        ind=2 #define an index variable
        while ind<=length/2:
            if word[ind-1]==word[-1*ind]: #compare the next character after the first, and last - working the way towards the center
                ind=ind+1 #incrememnt index to move onto the next pair of characters
                #print('index:',ind)
                #print('negative index:',-1*ind)
                #print(word[ind-1])
                #print(word[-1*ind])
            else: #after working halfway through the word, the while loop gets stopped
                ind=length
        print('You appear to have entered a palindrome')   
    else:
        print('You need to enter a string at least one character.')

            
