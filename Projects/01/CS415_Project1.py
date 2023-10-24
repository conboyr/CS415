from math import gcd
import random
import binascii
from re import I


def fmul(p1,q1,p2,q2):
    p = p1 * p2
    q = q1 * q2
    d = gcd(p, q)
    print(p,q)
    return (p/d, q/d)   

def fdiv(p1,q1,p2,q2):
    p = p1 * q2
    q = q1 * p2
    d = gcd(p, q)
    print(p,q)
    return (p/d, q/d)

def fadd(p1,q1,p2,q2):
    p = ((p1*q2) + (p2*q1) )
    q = q1 * q2
    d = gcd(p, q)
    print(p,q)
    return (p/d, q/d)

def fsub(p1,q1,p2,q2):
    p = ((p1*q2) - (p2*q1) )
    q = q1 * q2
    d = gcd(p, q)
    print(p,q)
    return (p/d, q/d)

def equal(p1,q1,p2,q2):
    d = gcd(p1, q1)
    e = gcd(p2, q2)
    f1 = (p1/d, q1/d)
    f2 = (p2/e, q2/e)
    if (f1 == f2):
        return True
    return False 

def less(p1,q1,p2,q2):
    d = gcd(p1, q1)
    e = gcd(p2, q2)
    p1 = (p1/d)
    p2 = (p2/e)
    q1 = (q1/d)
    q2 = (q2/e)
    if (q1 > q2):
        if (p1 <= p2):
            return True
    return False

def stringToBinary(string):
    binary = ''
    for char in string:
        binary += bin(ord(char))[2:].zfill(8) + ' '
    return binary[:-1]

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# Problem 1a:
def hsum(n):
    j = 1
    sum1 = (0,1)
    while (int(sum1[0]/sum1[1]) < n):
        sum1 = fadd(int(sum1[0]),int(sum1[1]),1,int(j))
        j = j+1
    return j


# Problem 1b:
def Fibonacci(n):
    if n == 0:
        print('Not a valid input')
        return 0
    i = 2
    f0 = (1,2)
    f1 = (1,3)
    fn = [0] * n
    fn[0] = f0
    if (n > 1):
        fn[1] = f1
    while (i < n):
        fn[i] = fadd(int(fn[i-2][0]),int(fn[i-2][1]),int(fn[i-1][0]),int(fn[i-1][1]))
        i = i + 1
    if (n > 1):
        return fn[i-1]
    else:
        return fn[i-2]    

# Problem 2:
def primality2(n,k):
    c = 0
    while (c < k):
        a = random.randrange(1, n-1)
        if (pow(a, n-1, n) == 1):
            c = c + 1
        else:
            return "no"
    return "yes"
            
def primality3(n,k):
    if (n % 3 == 0):
        return "no"
    if (n % 5 == 0):
        return "no"
    if (n % 7 == 0):
        return "no"
    if (n % 11 == 0):
        return "no"
    else: 
        return primality2(n, k)

# Problem 3

def bString(n,k):
    a = random.getrandbits(n-2)
    #bStr = format(a,'0b')
    bStr = bin (a)[2:].zfill(n-2)
    bStr = ("1" + bStr + "1")
    bStr = int(bStr, 2)
    isPrime = primality3(bStr,k)
    while (isPrime == "no"):
        a = random.getrandbits(n-2)
        #bStr = format(a,'0b')
        bStr = bin (a)[2:].zfill(n-2)
        bStr = ("1" + bStr + "1")
        bStr = int(bStr, 2)
        isPrime = primality3(bStr,k)
    
    return bStr

# Problem 4

def generate(n,k):
    p = bString(n,k)
    q = bString(n,k)
    N = p*q
    f = (p-1)*(q-1)
    E = random.getrandbits(10)
    while (gcd(E, f) != 1):
        E = random.getrandbits(10)
    D = modinv(E, f)
    return(N, E, D)

def encrypt(M, n, k):
    
    N, E, D = generate(n,k) 
    
    en = pow(M, E, N)
    de = pow(en, D, N)
    
    print ('\n Original Message:  ', M)
    print (' Encrypted Message: ', en) 
    print (' Message Decrypted: ', de)
    print ('\n Is Decryption == Message?')
    if de == M:
        return (' yes')
    else: return (' no')
    
    

def main():
    option = '0'
    while option != '5':
        
        print('\n Option 1: Problem 1a \n Option 2: Problem 1b \n Option 3: Problem 2 \n Option 4: Problem 5 \n Option 5: Quit')
        
        option = input('\n Enter a number to pick an option: ')
        print (' You entered: ', option)
    
        if option == '1':
            n = int(input (' Rewritten hsum function \n Enter a positive integer: '))
            print(hsum(n))
            
        elif option == '2':
            n = int(input (' Fibonacci function \n Enter a positive integer: '))
            print(Fibonacci(n))
            
        elif option == '3':
            n = int(input (' Primality Test function \n Enter a positive integer: '))
            k = int(input (' Enter a confidence parameter'))
            print (primality2(n, k))
            
        elif option == '4':
            M = int(input ('\n RSA Encryption algorithm \n Enter a number to be encrypted: '))    
            n = int(input (' Enter a number for size of n-bit integer: '))
            k = int(input (' Enter a number for the confidence parameter: '))
            print(encrypt(M, n, k))
            
    print ('\n Quitting Program...')
    
    
if __name__=="__main__":
    main()
  

    





