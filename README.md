# What is Ceaser Cypher?
Ceaser Cypher is one of the simplest and oldest encryption technique used in good old days. I
t is a type of substitution cipher where each letter in the plaintext is replaced by a letter a fixed number of positions down the alphabet.

# How it works
* Encryption Process
1. Choose a Shift Value: The sender and receiver must agree on a shift value, often referred to as the key. For example, a shift of 3 means that each letter will be replaced by the letter three places down the alphabet.
2. Substitution: Each letter in the plaintext is substituted based on the chosen shift. For instance:
  - A becomes D
  - B becomes E
  - C becomes F
  - ... and so on.
  - If the shift goes past Z, it wraps around to the beginning of the alphabet (e.g., X becomes A with a shift of 3).
  
# Example of Encryption
**To encrypt the phrase "HELLO" with a shift of 3:**
| Plaintext | Ciphertext |
|-----------|------------|
| H         | K          |
| E         | H          |
| L         | O          |
| L         | O          |
| O         | R          |
**The encrypted message would be "KHOOR" 34.**
# Decryption Process
**To decrypt a message, the receiver subtracts the same shift value from each letter:**

| Ciphertext | Plaintext |
|-----------|------------|
| K         | H          |
| H         | E          |
| O         | L          |
| O         | L          |
| R         | O          |

**Thus, "KHOOR" is decrypted back to "HELLO" 23.**
​# Mathematical Representation 
 `(x)=(x+n)mod26`
​
**(x) is the encrypted letter**

x is the original letter's position in the alphabet (A=0, B=1, ..., Z=25), and 
n is the shift value 6.

# Code Brakthrough 
1. `main.py`
  **Rich is a Python library for rich text and beautiful formatting in the terminal. [Rich Gihub LInk](https://github.com/Textualize/rich)**

```
 from ceaser_algo.main import encrypt, decrypt
 from rich import print

  def main():
      '''
      1. takes input from user (plaintext)
      2. takes int number of letters to shift from left to right 
      3. encrypt(arg1, arg2) takes plaintext and number to go from left to right
      4. prints the encrypted plain text on the console 
  
      decrypt(arg1, arg2) does exactly same as encrypt 
      '''
      # encrypt the plaintext
      user_input = input('enter str: ')
      input_shift = int(input('enter shift: '))
      e = encrypt(user_input, input_shift)
      print(f'[bold green]Your encrypted hash:[/bold green] [bold blue]{e}[/bold blue]')
  
      print('[bold magenta]Decrypt[/bold magenta]')
  
      # decrypt the encrypted text
      user_input = input('enter decrypted hash value: ')
      d = decrypt(user_input, input_shift)
      print(f'[bold green]Your decrypted hash:[/bold green] [bold blue]{d}[/bold blue]')
  
  # this block of code ensures that main() function runs only when this script is called not when imported as a Module
  if __name__ == "__main__":
      main()
```

2. From `ceaser_algo` module
   ***Explanation of code is in code itself***
# Encrypt function explanation
```
def encrypt(plaintext, n) -> str:
    '''
    1. accepts palintext and int 
    2. create an empty list and empty string variable
        a. empty list: to store the index of letters 
        b. result string: to store list of shifted letters to plain text as a string 
    3. try/catch block to handle Exception
    4. loop through plaintext
        a. find the index of user plaintext 
        b. find the index of next word for instance.
            i. if user passes ab as a string and 3 as a n parameter. shifted index and word would be a would have 3 as an index and string becomes d 
                and b would have 4 as an index and string becomes e
        c. then append shifted word to an empty_list 
    5. loop through the appended list
        a. add string to result variable to get plain text on the console

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
```
# Decrypt function explanation

```
def decrypt(plaintext, n) -> str:
    '''
    1. accepts palintext and int 
    2. create an empty list and empty string variable
        a. empty list: to store the index of letters 
        b. result string: to store list of shifted letters to plain text as a string 
    3. try/catch block to handle Exception
    4. loop through plaintext
        a. find the index of user plaintext 
        b. find the index of next word for instance. d -> 
            i. if user passes de as an encrypted string and 3 as a n parameter. reversed shifted index would have 1 as an index and string becomes a 
                and e would have 2 as an index and string becomes b
        c. then append shifted word to an empty_list 
    5. loop through the appended list
        a. add string to result variable to get plain text on the console
        
    '''
    shift_word, result = [], ''
    try:
        for i in plaintext: 
            find_index =(LETTERS.find(i)) 
            next_word = (find_index - n ) % len(LETTERS)   # 27 % 26 = 1 therefore the result is a

            shift_word.append(LETTERS[next_word])
    except Exception as err:
        print('[bold red]error[/bold red]')
    for i in shift_word:
        result += i 
    return result
```

