import pytest

def add(a, b):
    return a + b

def subtract(a, b):
    return a + b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def fizzbuzz(n):
    if not isinstance(n, int):
        #return 'fail'
        raise TypeError('Input must be an integer') 
    if n<=0:
        raise ValueError('Input must be positive') 
    
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return n
    
""" def test_fizzbuzz():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(3) == 'fizz'
    assert fizzbuzz(5) == 'buzz'
    assert fizzbuzz(15) == 'fizzbuzz'

    with pytest.raises(TypeError):
        fizzbuzz(2.5)
    
    with pytest.raises(ValueError):
        fizzbuzz(-1) """


def convert_fahrenheit_to_celsius(fahrenheit):
    return multiply(subtract(fahrenheit, 32), 9 / 5) # <-- Fix this in step 7
