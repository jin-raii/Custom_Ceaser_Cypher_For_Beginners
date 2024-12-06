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
`
H → K_
E → H
L → O
L → O
O → R`
**The encrypted message would be "KHOOR" 34.**
# Decryption Process
**To decrypt a message, the receiver subtracts the same shift value from each letter:**
`K → H
H → E
O → L
O → L
R → O`
**Thus, "KHOOR" is decrypted back to "HELLO" 23.**
​# Mathematical Representation 
 `(x)=(x+n)mod26`
​
**(x) is the encrypted letter**

x is the original letter's position in the alphabet (A=0, B=1, ..., Z=25), and 
n is the shift value 6.


