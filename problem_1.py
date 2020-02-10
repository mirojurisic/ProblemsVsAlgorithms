import math


def sqrt(number):
    """
    Calculate the floored square root of a number
    The expected time complexity is O(log(n))


    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number <= 1:
        return number

    def recursion(down, up):
        if number // up == up:
            return up
        if number // down == down:
            return down
        guess = (down + up) // 2
        if guess == down: # if difference between down and up is one, this means that down is solution
            return down
        if number // guess == guess:
            return guess
        if number // guess < guess:
            return recursion(down, guess)
        else:
            return recursion(guess, up)

    result = recursion(1, number // 2)
    return result


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (7 == sqrt(55)) else "Fail")
print("Pass" if (9 == sqrt(99)) else "Fail")
