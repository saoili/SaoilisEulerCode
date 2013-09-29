import math

def primes (n): 
    """Returns a list of primes up to and including n (if prime)"""
    return noBlanks(sieve(n))  

def sieve (n):
    """Returns a list, (0,n), where the ith element is i if prime and 0 otherwise"""
    primes = range (0,n+1)
    primes [1] = 0
    for i in range (2,n):
        for j in range (2,(int)(n/i)+1):
            primes [i*j] = 0
    return primes

def addToSieve(n, sieve): 
    """Takes a sieved list of primes (with spaces still in) and an integer n. 
    Returns a sieve up to n"""
    lenSieve = len(sieve) 
    if lenSieve > n: 
        return sieve 
    primes = sieve 
    for i in range (lenSieve,n+1): 
        primes.append(i) 
    for i in range (2,n): 
        if i == 0: 
            break
        for j in range(2,(int)(n/i)+1): 
            primes[i*j] = 0
    return primes 

def noBlanks (li):
    """takes a list and returns all non zero elements of that list, as a list"""
    retVal = []
    for i in range (0,len(li)):
        if li[i] != 0:
            retVal.append(li[i])
    return retVal

def distPrimeFacts (n,lSieve): 
    """returns a list of the distinct prime factors of positive integer n.
    Take lSieve to be a sieve, adds to it if it's length is less than n.
    """ 
    if type(n) != int or n < 1: 
        print "Error in distinctPrimeFactors, only positive integers allowed"
        return [] 
    if lSieve == []: 
        newSieve = sieve(n) 
    else: 
        newSieve = addToSieve(n,lSieve) 
    primes = noBlanks(newSieve) 
    distPrimeFacts = [] 
    for prime in primes: 
        if n % prime == 0: 
            distPrimeFacts.append(prime) 
            while n % prime == 0: 
               n = n/prime 
    return distPrimeFacts, newSieve    


def pentN (n):
    """takes integer n, returns the nth pentagonal number"""
    return n*(3*n-1)/2

def isPent(n):
    """takes integer n, returns True if it is a pentagonal number, else False
    returns False for negative numbers"""
    if n < 0:
        return False
    return ((math.sqrt(24*n+1)+1)/6)==int(((math.sqrt(24*n+1)+1)/6))

def nthPent(n):
    """takes integer n, returns what number pentagonal number it is if it is one and 0 otherwise"""
    if not isPent(n):
        return 0
    return (int)((math.sqrt(24*n+1)+1)/6)


def triN (n):
    """takes integer n, returns the nth triangular number"""
    return n*(n+1)/2

def isTri(n):
    """doesn't work yet!
    takes integer n, returns True if it is a triangular number, else False
    returns False for negative numbers"""
    if n < 0:
        return False
    return False


def hexN(n):
    """takes integer n, returns the nth hexagonal number"""
    return n*(2*n-1)



def nthDigit (x,n):
    """(x,n) returns the nth digit of x, returns -1 if that digit doesn't exist"""
    if n < 0 or n > numDigits(x):
        return -1
    x = reverse(x)
    return int(round(x%pow(10,n)/pow(10,n-1)))

def numDigits (n):
    """returns the number of digits in a positive integer with up to 9 digits"""
    if n < 10:
        return 1
    if n < 100:
        return 2
    if n < 1000:
        return 3
    if n < 10000:
        return 4
    if n < 100000:
        return 5
    if n < 1000000:
        return 6
    if n < 10000000:
        return 7
    if n < 100000000:
        return 8
    return 9

def isPrime(n):
    """returns True if prime, False if not. For large selections of numbers, use sieve instead"""
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    for i in range (1,(int(pow(n, .5))+1)/2):
        if n % (i*2+1) == 0:
            return False
    return True

def reverse(n):
    """returns the reverse of a positive integer"""
    digs = numDigits(n)
    if digs == 1:
        return n
    retVal = 0
    for i in range (0,digs):
        retVal = retVal + n % pow(10,digs-i)/pow(10,digs-(1+i)) * pow(10,i)
    return retVal

def isPandigital(n):
    """returns true if n is a 1 to 9 pandigital"""
    if numDigits(n) != 9:
        return False
    blah = n
    digs = []
    while blah >= 1:
        digs.append(blah%10)
        blah = blah / 10
    return 1 in digs and 2 in digs and 3 in digs and 4 in digs and 5 in digs and 6 in digs and 7 in digs and 8 in digs and 9 in digs

if __name__ == "__main__":
    "Should put some testing stuff in here for useful functions, haven't yet"""
    print "This is a module of useful functions for Project Euler problems"






