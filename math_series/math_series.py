def fibonacci(n):
    """This function returns the nth value in the fibonacci series. 'n' being it's input integer."""
    if n <= 1:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """This function returns the nth value in the lucas series. 'n' being it's input integer."""
    if n <= 1:
        return 2 - n 
    else:
        return lucas(n-1) + lucas(n-2)


def other_series(n, x, y):
    """This function returns the nth value in a sum series. 'n' being it's input integer.
    'x' being it's first value and 'y' it's second."""
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return other_series(n-1, x, y) + other_series(n-2, x, y)


def sum_series(n, x=0, y=1):
    """This function returns the nth value in the fibonacci or lucas series. 'n' being it's input integer.
    This function takes in two other optional parameters. By default they are 0 and 1; these values represent
    the first two numbers in the series (since fionacci starts with 0,1 and lucas with 2,1)"""
    if x == 0 and y == 1:
        return fibonacci(n)
    
    if x == 2 and y == 1:
        return lucas(n)

    return other_series(n, x, y)     