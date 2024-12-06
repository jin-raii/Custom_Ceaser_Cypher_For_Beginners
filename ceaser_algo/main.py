'''
e = (a + n) mod 26
a is original number
n is shift 

if you want to encrypt the word “Python” with the key 4, 
you’ll add 4 LETTERS in the alphabet to each character of “
Python”. Since “P” is the 16° letter, you know that the result is “T”, the 20° letter. 
Keep doing that, you’re gonna end up with ”Tcxlsr”.
If the result is greater than 26, you simply loop into the alphabet (27=a).

'''

import random

LETTERS =  'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+'
LETTERS.join(random.sample(LETTERS, len(LETTERS)))

def encrypt(plaintext, n) -> str:
    '''
    encrypt the plaintext
    '''
    shift_word, result = [], ''
    try:
        for i in plaintext: 
            find_index =(LETTERS.find(i))
            next_word = (find_index + n ) % len(LETTERS) # 27 % 26 = 1 therefore the result is a       
            shift_word.append(LETTERS[next_word])
    except Exception as err:
        print('[bold red]error[/bold red]')
    for i in shift_word:
        result += i
    
    return result

def decrypt(plaintext, n) -> str:
    '''
    decrypt the encrypted text 
    
    '''
    shift_word, result = [], ''
    try:
        for i in plaintext: 
            find_index =(LETTERS.find(i)) 
            next_word = (find_index - n ) % len(LETTERS)   # 27 % 26 = 1 therefore the result is a
            # index_of_plaintext.append(find_index) 
            shift_word.append(LETTERS[next_word])
    except Exception as err:
        print('[bold red]error[/bold red]')
    for i in shift_word:
        result += i 
    return result
