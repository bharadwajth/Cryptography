#!/usr/bin/python3

def FindGCD(a,b):
    prevx, x = 1, 0; prevy, y = 0, 1
    while b:
        q = a/b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a % b
    return a, prevx, prevy

p = input("Enter a prime p: ") # Get Prime 'p'
q = input("Enter a prime q: ") # Get Prime 'q'

n = p*q # Calculate n
print("n: " + str(n))

totient = (p-1)*(q-1)
print("Totient: " + str(totient))

for i in range (2,totient):
    x, y, z = FindGCD(i,totient)   
    if(x == 1):
        print("e: " + str(i))
        print("d: " + str(y))
        break

