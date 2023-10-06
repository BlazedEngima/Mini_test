from math import sqrt

array = [x for x in range(1, 101)]

def isPrime(num):
    if num <= 1:
        return False

    # Checks if num is divisible by any number from 2 to sqrt(num)
    # Since if num is not prime, then one of the roots must be lower
    # than the root of num.
    for div in range(2, int(sqrt(num) + 1)):
        if num % div == 0:
            return False

    return True

if __name__ == "__main__":
    # Output string
    output = ''

    # Main algorithm
    for x in range(len(array) - 1, -1, -1):
        if isPrime(array[x]):
            continue
        
        temp = ''
        if array[x] % 3 == 0: temp += 'Foo' 
        if array[x] % 5 == 0: temp += 'Bar'

        if temp == '': output += str(array[x])

        # Append temp to output string
        output += temp
        # Exclude adding comma and space for the last element
        if x != 0:
            output += ', '
        

    print(output)
