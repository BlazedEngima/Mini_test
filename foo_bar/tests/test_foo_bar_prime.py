from foo_bar import isPrime

def test_isPrime():
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(5) == True
    assert isPrime(6) == False
    assert isPrime(7) == True
    assert isPrime(8) == False
    assert isPrime(9) == False
    assert isPrime(10) == False
    assert isPrime(11) == True