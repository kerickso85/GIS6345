def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome():
    print("Please enter a single word to determine if it is a palindrome:")
    word=input('>>>')
    length=len(word)
    print('Number of characters in the word are: ',length)

    if length = 1:
        print('Yes, your single character is technically a palindrome. But a lame one at that...')
    elif length%2>0:
        print('Your word has an even number of characters, therefore it cannot be a palindrome.')
    else:
        
    
