import math


def primes(n):
    """Returns a list of primes up to and including n (if prime)"""
    return noBlanks(sieve(n))


def sieve(n):
    """Returns a list, [0, ... ,n], where the ith element is 
    i if prime and 0 otherwise"""
    primes = [i for i in range(0, n+1)]
    primes[1] = 0
    for i in range(2, n):
        for j in range(2, (int)(n//i)+1):
            primes[i*j] = 0
    return primes


def addToSieve(n, sieve):
    """Takes a sieved list of primes (with spaces still in) 
    and an integer n. Returns a sieve up to n"""
    lenSieve = len(sieve)
    if lenSieve > n:
        return sieve
    primes = sieve
    for i in range(lenSieve, n+1):
        primes.append(i)
    for i in range(2, n):
        if i == 0:
            break
        for j in range(2, (int)(n//i)+1):
            primes[i*j] = 0
    return primes


def noBlanks(li):
    """takes a list and returns all non zero elements of that list, 
    as a list"""
    retVal = []
    for i in range(0, len(li)):
        if li[i] != 0:
            retVal.append(li[i])
    return retVal


def distPrimeFacts(n, lSieve):
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
        newSieve = addToSieve(n, lSieve)
    primes = noBlanks(newSieve)
    distPrimeFacts = []
    for prime in primes:
        if n % prime == 0:
            distPrimeFacts.append(prime)
            while n % prime == 0:
                n = n//prime
    return distPrimeFacts, newSieve


def distinctPrimeFactors(n):
    """returns a list of the distinct prime factors 
    of positive integer n"""
    a, b = distPrimeFacts(n, [])
    return a


def divisors(n):
    """
    returns an ordered list of all divisors of positive integer n
    Note: this includes n, so is not 'proper divisors'
    """
    divs = []
    for i in range(1, n+1):
        if n % i == 0:
            divs.append(i)

    return divs


def pentN(n):
    """takes integer n, returns the nth pentagonal number"""
    return n*(3*n-1)//2


def isPent(n):
    """takes integer n, returns True if it is a pentagonal number, 
    else False
    returns False for negative numbers"""
    if n < 0:
        return False
    return ((math.sqrt(24*n+1)+1)/6) == int(((math.sqrt(24*n+1)+1)/6))


def nthPent(n):
    """takes integer n, returns what number pentagonal number 
    it is if it is one and 0 otherwise"""
    if not isPent(n):
        return 0
    return (int)((math.sqrt(24*n+1)+1)//6)


def triN(n):
    """takes integer n, returns the nth triangular number"""
    return n*(n+1)//2


def hexN(n):
    """takes integer n, returns the nth hexagonal number"""
    return n*(2*n-1)


def nthDigit(x, n):
    """(x,n) returns the nth digit of x, 
    returns -1 if that digit doesn't exist"""
    if n < 0 or n > numDigits(x):
        return -1
    x = reverse(x)
    return int(round(x % pow(10, n)//pow(10, n-1)))


def numDigits(n):
    """returns the number of digits in an integer"""
    return len(str(abs(n)))


def isPrime(n):
    """returns True if prime, False if not. 
    For large selections of numbers, use sieve instead"""
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    for i in range(1, (int(pow(n, .5))+1)//2):
        if n % (i*2+1) == 0:
            return False
    return True


def reverse(n):
    """returns the reverse of a positive integer"""
    digs = numDigits(n)
    if digs == 1:
        return n
    retVal = 0
    for i in range(0, digs):
        retVal = retVal + n % pow(10, digs-i)//pow(10, digs-(1+i)) * pow(10, i)
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
        digs.append(blah % 10)
        blah = blah//10
    return (
        1 in digs and 2 in digs and 3 in digs and 4 in digs and 5 in digs and
        6 in digs and 7 in digs and 8 in digs and 9 in digs and 0 in digs)


def print_test_failure(func, inputs, expected, actual):
    print(f"for function {func.__name__}, with input(s) {inputs}", end=" ")
    print(f"expected was {expected} and actual was {actual}")


def run_tests():
    allFine = True

    """test primes (n): 
    Returns a list of primes up to and including n (if prime)"""
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    actual = primes(100)
    if expected != actual:
        allFine = False
        print_test_failure(primes, 100, expected, actual)

    """test sieve (n):
    Returns a list, [0, ... ,n], where the ith element is i if prime 
    and 0 otherwise"""
    expected = [0, 0, 2, 3, 0, 5, 0, 7, 0, 0, 0]
    actual = sieve(10)
    if expected != actual:
        allFine = False
        print_test_failure(sieve, 10, expected, actual)

    """test addToSieve(n, sieve): 
    Takes a sieved list of primes (with spaces still in) 
    and an integer n. Returns a sieve up to n"""
    expected = [0, 0, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19, 0]
    actual = addToSieve(20, sieve(10))
    if expected != actual:
        allFine = False
        print_test_failure(addToSieve, (20, sieve(10)), expected, actual)

    """test noBlanks (li):
    takes a list and returns all non zero elements of that list, 
    as a list"""
    expected = [1, 2, 3, 5]
    actual = noBlanks([0, 1, 2, 3, 0, 0, 5, 0])
    if expected != actual:
        allFine = False
        print_test_failure(noBlanks, [0, 1, 2, 3, 0, 0, 5, 0], expected, actual)

    """test distinctPrimeFactors (n,lSieve): 
    returns a list of the distinct prime factors of positive integer n
    """
    expected = distinctPrimeFactors(70) 
    actual = [2, 5, 7]
    if expected != actual:
        allFine = False
        print_test_failure(distinctPrimeFactors, 70, expected, actual)

    """test divisors(n):
    returns a list of all divisors of n
    """
    expected1 = [1]
    expected2 = [1, 2, 3, 5, 6, 10, 15, 30]
    expected3 = [1, 7]
    actual1 = divisors(1)
    actual2 = divisors(30)
    actual3 = divisors(7)
    if expected1 != actual1 or expected2 != actual2 or expected3 != actual3:
        allFine = False
        print_test_failure(divisors, 1, expected1, actual1)
        print_test_failure(divisors, 30, expected2, actual2)
        print_test_failure(divisors, 7, expected3, actual3)

    """test pentN (n):
    takes integer n, returns the nth pentagonal number"""
    expected1 = 1
    expected2 = 145
    expected3 = 590
    actual1 = pentN(1)
    actual2 = pentN(10)
    actual3 = pentN(20)

    if expected1 != actual1 or expected2 != actual2 or expected3 != actual3:
        allFine = False
        print_test_failure(pentN, 1, expected1, actual1)
        print_test_failure(pentN, 10, expected2, actual2)
        print_test_failure(pentN, 20, expected3, actual3)

    """test isPent(n):
    takes integer n, returns True if it is a pentagonal number, 
    else False
    returns False for negative numbers"""
    expected1 = False
    expected2 = True
    expected3 = False
    actual1 = isPent(377)
    actual2 = isPent(782)
    actual3 = isPent(-10)

    if expected1 != actual1 or expected2 != actual2 or expected3 != actual3:
        allFine = False
        print_test_failure(isPent, 377, expected1, actual1)
        print_test_failure(isPent, 782, expected2, actual2)
        print_test_failure(isPent, -10, expected3, actual3)
    
    """test nthPent(n):
    takes integer n, returns what number pentagonal number it is 
    if it is one and 0 otherwise"""
    isNthPentWorking = nthPent(925) == 25 and nthPent(1000) == 0
    if not isNthPentWorking:
        allFine = False

    """test triN (n):
    takes integer n, returns the nth triangular number"""
    isTriNWorking = triN(0) == 0 and triN(10) == 55
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
    isNthDigitWorking = nthDigit(4321, 3) == 2 and nthDigit(2, 2) == -1
    if not isNthDigitWorking:
        allFine = False

    """test numDigits (n):
    returns the number of digits in a positive integer 
    with up to 9 digits"""
    expected1 = 1
    expected2 = 2
    expected3 = 9
    expected4 = 2
    actual1 = numDigits(1)
    actual2 = numDigits(11)
    actual3 = numDigits(111345151)
    actual4 = numDigits(-78)

    if (
        expected1 != actual1 or expected2 != actual2
        or expected3 != actual3 or expected4 != actual4
    ):
        allFine = False
        print_test_failure(numDigits, 1, expected1, actual1)
        print_test_failure(numDigits, 11, expected2, actual2)
        print_test_failure(numDigits, 111345151, expected3, actual3)
        print_test_failure(numDigits, -78, expected4, actual4)

    """test isPrime(n):
    returns True if prime, False if not. 
    For large selections of numbers, use sieve instead"""
    isIsPrimeWorking = isPrime(997) and not isPrime(993)
    if not isIsPrimeWorking:
        allFine = False

    """test reverse(n):
    returns the reverse of a positive integer"""
    isReverseWorking = (reverse(12345) == 54321 and reverse(1) == 1 and
                        reverse(12321) == 12321)
    if not isReverseWorking:
        allFine = False

    """test isPandigital(n):
    returns true if n is a 1 to 9 pandigital"""
    expected1 = True
    expected2 = True
    expected3 = False
    actual1 = isPandigital(1223334444555567890)
    actual2 = isPandigital(1023456879)
    actual3 = isPandigital(123456789)

    if expected1 != actual1 or expected2 != actual2 or expected3 != actual3:
        allFine = False
        print_test_failure(isPandigital, 1223334444555567890, expected1, actual1)
        print_test_failure(isPandigital, 1023456879, expected2, actual2)
        print_test_failure(isPandigital, 123456789, expected3, actual3)

    if allFine:
        print("Excellent, everything worked, carry on")
    else:
        print("oh oh, something failed, scroll up for details")


if __name__ == "__main__":
    print("This is a module of useful functions for Project Euler problems")
    print("Some basic testing below, will replace with unittest framework later")
    run_tests()
    