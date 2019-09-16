import math

def primes (n): 
    """Returns a list of primes up to and including n (if prime)"""
    return noBlanks(sieve(n))  

def sieve (n):
    """Returns a list, [0, ... ,n], where the ith element is 
    i if prime and 0 otherwise"""
    primes = [i for i in range (0,n+1)]
    primes[1] = 0
    for i in range (2,n):
        for j in range (2,(int)(n//i)+1):
            primes[i*j] = 0
    return primes

def addToSieve(n, sieve): 
    """Takes a sieved list of primes (with spaces still in) 
    and an integer n. Returns a sieve up to n"""
    lenSieve = len(sieve) 
    if lenSieve > n: 
        return sieve 
    primes = sieve 
    for i in range (lenSieve,n+1): 
        primes.append(i) 
    for i in range (2,n): 
        if i == 0: 
            break
        for j in range(2,(int)(n//i)+1): 
            primes[i*j] = 0
    return primes 

def noBlanks (li):
    """takes a list and returns all non zero elements of that list, 
    as a list"""
    retVal = []
    for i in range (0,len(li)):
        if li[i] != 0:
            retVal.append(li[i])
    return retVal

def distPrimeFacts (n,lSieve): 
    """returns a list of the distinct prime factors 
    of positive integer n and a sieve of primes up to that number.
    Take lSieve to be a sieve, adds to it if it's length is less than n.
    """ 
    if type(n) != int or n < 1: 
        print("Error in distinctPrimeFactors, only positive integers allowed")
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
               n = n//prime 
    return distPrimeFacts, newSieve    

def distinctPrimeFactors (n):
   """returns a list of the distinct prime factors 
   of positive integer n"""
   a, b = distPrimeFacts(n,[])
   return a
    


def pentN (n):
    """takes integer n, returns the nth pentagonal number"""
    return n*(3*n-1)//2

def isPent(n):
    """takes integer n, returns True if it is a pentagonal number, 
    else False
    returns False for negative numbers"""
    if n < 0:
        return False
    return ((math.sqrt(24*n+1)+1)/6)==int(((math.sqrt(24*n+1)+1)/6))

def nthPent(n):
    """takes integer n, returns what number pentagonal number 
    it is if it is one and 0 otherwise"""
    if not isPent(n):
        return 0
    return (int)((math.sqrt(24*n+1)+1)//6)


def triN (n):
    """takes integer n, returns the nth triangular number"""
    return n*(n+1)//2


def hexN(n):
    """takes integer n, returns the nth hexagonal number"""
    return n*(2*n-1)



def nthDigit (x,n):
    """(x,n) returns the nth digit of x, 
    returns -1 if that digit doesn't exist"""
    if n < 0 or n > numDigits(x):
        return -1
    x = reverse(x)
    return int(round(x%pow(10,n)//pow(10,n-1)))

def numDigits (n):
    """returns the number of digits in an integer"""
    return len(str(abs(n)))


def isPrime(n):
    """returns True if prime, False if not. 
    For large selections of numbers, use sieve instead"""
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    for i in range (1,(int(pow(n, .5))+1)//2):
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
        retVal = retVal + n % pow(10,digs-i)//pow(10,digs-(1+i)) * pow(10,i)
    return retVal

def isPandigital(n):
    """returns true if n is a 1 to 9 pandigital"""
    """this originally returned false if not equal to 9
    this was working because numDigits currently returns 9 if there 
    are greater than 9 digits. If numDigits is extended later,
    this would have broken. Changed."""
    if numDigits(n) < 9:
        return False
    blah = n
    digs = []
    while blah >= 1:
        digs.append(blah%10)
        blah = blah//10
    return (
       1 in digs and 2 in digs and 3 in digs and 4 in digs and 5 in digs and
       6 in digs and 7 in digs and 8 in digs and 9 in digs and 0 in digs)

if __name__ == "__main__":
    print("This is a module of useful functions for Project Euler problems")
    print("Some basic testing below, will replace with unittest framework later")
    allFine = True
    
    """test primes (n): 
    Returns a list of primes up to and including n (if prime)"""
    isPrimeWorking = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
                      53, 59, 61, 67, 71, 73, 79, 83, 89, 97] == primes(100)
    if not isPrimeWorking:
        allFine = False
     
    """test sieve (n):
    Returns a list, [0, ... ,n], where the ith element is i if prime 
    and 0 otherwise"""
    isSieveWorking = [0,0,2,3,0,5,0,7,0,0,0] == sieve(10)
    if not isSieveWorking:
        allFine = False
        
    """test addToSieve(n, sieve): 
    Takes a sieved list of primes (with spaces still in) 
    and an integer n. Returns a sieve up to n"""
    isAddToSieveWorking = [0,0,2,3,0,5,0,7,0,0,0,11,0,13,0,0,0,17,0,
                           19,0] == addToSieve(20, sieve(10))
    if not isAddToSieveWorking:
        allFine = False
        
    """test noBlanks (li):
    takes a list and returns all non zero elements of that list, 
    as a list"""
    isNoBlanksWorking = [1,2,3,5] == noBlanks([0,1,2,3,0,0,5,0])
    if not isNoBlanksWorking:
        allFine = False
        
    """test distinctPrimeFactors (n,lSieve): 
    returns a list of the distinct prime factors of positive integer n
    """ 
    isDistinctPrimeFactorsWorking = distinctPrimeFactors(70) == [2,5,7]
    if not isDistinctPrimeFactorsWorking:
        allFine = False
            
    """test pentN (n):
    takes integer n, returns the nth pentagonal number"""
    isPentNWorking = pentN (1) == 1 and pentN(10) == 145 and pentN(20) == 590
    if not isPentNWorking:
        allFine = False
    
    """test isPent(n):
    takes integer n, returns True if it is a pentagonal number, 
    else False
    returns False for negative numbers"""
    isIsPentWorking = not isPent(377) and isPent(782) and not isPent(-10)
    if not isIsPentWorking:
        allFine = False

    """test nthPent(n):
    takes integer n, returns what number pentagonal number it is 
    if it is one and 0 otherwise"""
    isNthPentWorking = nthPent(925) == 25 and nthPent(1000) == 0
    if not isNthPentWorking:
        allFine = False

    """test triN (n):
    takes integer n, returns the nth triangular number"""
    isTriNWorking = triN(0)==0 and triN(10) == 55
    if not isTriNWorking:
        allFine = False
    
    """test hexN(n):
    takes integer n, returns the nth hexagonal number"""
    isHexNWorking = hexN(8) == 120 and hexN(18) == 630
    if not isHexNWorking:
        allFine = False

    """test nthDigit (x,n):
    (x,n) returns the nth digit of x, 
    returns -1 if that digit doesn't exist"""
    isNthDigitWorking = nthDigit(4321,3) == 2 and nthDigit (2,2) == -1
    if not isNthDigitWorking:
        allFine = False

    """test numDigits (n):
    returns the number of digits in a positive integer 
    with up to 9 digits"""
    isNumDigitsWorking = (numDigits(1) == 1 and numDigits(11) == 2 and 
                          numDigits(111) == 3 and numDigits(111111111) == 9 and
                          numDigits(-11) == 2)
    if not isNumDigitsWorking:
        allFine = False

    """test isPrime(n):
    returns True if prime, False if not. 
    For large selections of numbers, use sieve instead"""
    isIsPrimeWorking = isPrime(997) and not isPrime(993)
    if not isIsPrimeWorking:
        allFine = False

    """test reverse(n):
    returns the reverse of a positive integer"""
    isReverseWorking = (reverse(12345)==54321 and reverse(1) == 1 and
                        reverse (12321) == 12321)
    if not isReverseWorking:
        allFine = False
        
    """test isPandigital(n):
    returns true if n is a 1 to 9 pandigital"""
    isPandigitalWorking = (isPandigital(1223334444555567890) and
                           isPandigital (1023456879) and not
                           isPandigital (123456789))
    if not isPandigitalWorking:
        allFine = False
    

    if allFine:
        print("Excellent, everything worked, carry on"   )
    else:
        print("oh oh, something failed")
        print("primes function works for 100: " + str (isPrimeWorking))
        print("sieve function works for 10: " + str (isSieveWorking))
        print ("addToSieve function works for 20 and sieve up to 10: " +
              str (isAddToSieveWorking))
        print ("noBlanks function works for [0,1,2,3,0,0,5,0]: " +
              str(isNoBlanksWorking))
        print ("distinctPrimeFactors function works for 70: " +
              str(isDistinctPrimeFactorsWorking))
        print ("pentN function works for 1, 10, and 20: " +
              str(isPentNWorking))
        print ("isPent function works for 377 (false), "
               "782 (true), and -10 (false): " + str(isIsPentWorking))
        print ("nthPent function works for 925 (25) and 1000 (0): " +
              str(isNthPentWorking))
        print ("triN function works for 0 (0) and 10 (55): " +
              str(isTriNWorking))
        print ("hexN function works for 8 (120) and 18 (630): " +
              str(isHexNWorking))
        print ("nthDigit function works for (4321,3) (2) and (2,2) (-1): " +
              str(isNthDigitWorking))
        print ("numDigits function works for 1, 2, 3, or 9 '1's: " +
              str(isNumDigitsWorking))
        print ("isPrime function works for 997 (true) and 993 (false): " +
              str(isIsPrimeWorking))
        print ("reverse function works for 12345, 1, and 12321: " +
              str(isReverseWorking))
        print (("isPandigital function works for 1223334444555567890 (true) "+
              "and 1023456879 (true) and 123456789 (false): " +
              str(isPandigitalWorking)))
