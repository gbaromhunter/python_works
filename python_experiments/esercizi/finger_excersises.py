# Write a program that examines three variables—
# x, y, and z—and prints the largest odd number among them. If none
# of them are odd, it should print the smallest value of the three.
import random


def ex0(x, y, z):
    odd = [a for a in [x, y, z] if a % 2 != 0]
    even = [a for a in [x, y, z] if a % 2 == 0]
    if odd:
        return print(f"The largest odd number is: {max(odd)}")
    else:
        return print(f"The lowest number is: {min(even)}")


def ex1(x, y, z):
    odd = [a for a in [x, y, z] if a % 2 != 0]
    even = [a for a in [x, y, z] if a % 2 == 0]
    return print(max(odd)) if odd else print(min(even))


# the book answer
def ex2(x, y, z):
    answer = min(x, y, z)
    if x % 2 != 0:
        answer = x
    if y % 2 != 0 and y > answer:
        answer = y
    if z % 2 != 0 and z > answer:
        answer = z
    return print(answer)


# Write code that asks the user to enter their
# birthday in the form dd/mm/yyyy, and then prints a string of the
# form ‘You were born in the year yyyy.’

def bdyear():
    birthday = input(f"Insert your birthday in the form of dd/mm/yyyy")
    return print(f"You were born in the year {birthday[-4:]}")


# Replace the comment in the following code with a
# while loop


def x_many():
    num_x = int(input('How many times should I print the letter X? '))
    to_print = ''
    x = 0
    while x <= num_x:
        to_print = to_print + "X"
        x += 1
    print(to_print)


# Write a program that asks the user to input 10
# integers, and then prints the largest odd number that was entered. If
# no odd number was entered, it should print a message to that effect.


def ten_numbers():
    numbers = [int(input("Insert a number")) for n in range(10)]
    odds = [a for a in numbers if a % 2 != 0]
    if odds:
        return print(f"The highest odd number is: {max(odds)}")
    else:
        return print(f"There are no odd numbers!")


# Write a program that prints the sum of the prime
# numbers greater than 2 and less than 1000. Hint: you probably want
# to use a for loop that is a primality test nested inside a for loop that
# iterates over the odd integers between 3 and 999.


def sum_prime_numbers():
    return sum([a for a in range(3, 1000) if a % 2 != 0])


def is_prime_smallest():
    x = int(input("Insert a number greater than 2: "))
    smallest_divisor = None
    for guess in range(2, x):
        if x % guess == 0:
            smallest_divisor = guess
            break
    if smallest_divisor != None:
        print(f"The smallest divisor of {x} is {smallest_divisor}")
    else:
        print(f"{x} is a prime number")


# Change the code so that it returns
# the largest rather than the smallest divisor. Hint: if y*z = x and y is
# the smallest divisor of x, z is the largest divisor of x.


def is_prime_largest():
    x = int(input("Insert a number greater than 2: "))
    d = [a for a in range(2, x) if x % a == 0]
    if d:
        return print(f"The largest divisible is {max(d)}") if d else print(f"{x} is a prime number")


def is_prime(x):
    if not [a for a in range(2, x) if x % a == 0]:
        print(f"{x} is a prime number")
        return True
    else:
        print(f"{x} is not a prime number")
        return False


def is_prime_oneliner(x):
    return True if not [a for a in range(2, x) if x % a == 0] else False


def prime_list(n):
    return [x for x in range(3, n, 2) if not [a for a in range(2, x) if x % a == 0]]


# Write a program that asks the user to enter an
# integer and prints two integers, root and pwr, such that 1 < pwr < 6
# and root**pwr is equal to the integer entered by the user. If no such
# pair of integers exists, it should print a message to that effect.


def integer_pairs():
    x = int(input("Insert a number: "))
    for pwr in range(1, 7):
        for guess in range(2, x):
            if guess ** pwr == x:
                return print(f"The root is {guess} and the power is {pwr}")
    return print(f"There is no such number!")


# Write a program that prints the sum of the prime
# numbers greater than 2 and less than 1000. Hint: you probably want
# to have a loop that is a primality test nested inside a loop that
# iterates over the odd integers between 3 and 999.

def prime_sum():
    return sum([x for x in range(3, 1000, 2) if not [a for a in range(2, x) if x % a == 0]])


# This is simple algorithm to find square root of x

def square(x):
    epsilon = 0.01
    step = epsilon ** 2
    num_guesses = 0
    ans = 0.0
    while abs(ans ** 2 - x) >= epsilon and ans * ans <= x:
        ans += step
        num_guesses += 1
    print(f"Number of guesses is {num_guesses}")
    if abs(ans ** 2 - x) >= epsilon:
        print(f"Failed the square root of{x}")
    else:
        print(f"{ans} is close to square root of {x}")


# This is bisection algorithm for same problem

def bise_square(x):
    x = abs(x)
    epsilon = 0.01
    num_guesses = 0
    low = 0
    high = max(1, x)
    ans = (high + low) / 2
    while abs(ans ** 2 - x) >= epsilon:
        print(f"Low is {low}, High is {high}, Answer is {ans}")
        num_guesses += 1
        if ans ** 2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return print(f"Square root of {x} is about {ans} and it took {num_guesses} guesses")


# What would the code in Figure 3-5 do if x = -25?


# What would have to be changed to make the code
# in Figure 3-5 work for finding an approximation to the cube root of
# both negative and positive numbers? Hint: think about changing low
# to ensure that the answer lies within the region being searched.


def bise_cube(x):
    epsilon, num_guesses, low, high = 0.01, 0, 0, max(1, abs(x))
    ans = (high + low) / 2
    while abs(ans ** 3 - abs(x)) >= epsilon:
        print(f"Low is {low}, High is {high}, Answer is {ans}")
        num_guesses += 1
        if ans ** 3 < abs(x):
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    ans = -ans if x < 0 else ans
    return print(f"Cube root of {x} is about {ans} and it took {num_guesses} guesses")


# The Empire State Building is 102 stories high. A
# man wanted to know the highest floor from which he could drop an
# egg without the egg breaking. He proposed to drop an egg from the
# top floor. If it broke, he would go down a floor, and try it again. He
# would do this until the egg did not break. At worst, this method
# requires 102 eggs. Implement a method that at worst uses seven
# eggs.


def find_egg():
    egg = random.randint(1, 102)
    high, low, ng = 102, 1, 1
    ans = (high + low) // 2
    while ans != egg:
        if ans > egg:
            high = ans
        else:
            low = ans
        ans = (high + low) // 2
        ng += 1
    return print(f"The eggs should have broken at {egg}, we found that it breaks at {ans} with {ng} guesses")


# What is the decimal equivalent of the binary
# number 10011?


# Newton-Raphson for square root
# find x such that x**2 - k is within epsilon of 0
def square_newton(k):
    epsilon, c, guess = 0.01, 0, k / 2
    while abs(guess ** 2 - k) >= epsilon:
        print(f"Guess is {guess}")
        guess = guess - (((guess ** 2) - k) / (2 * guess))
        c += 1
    return print(f"Square root of {k} is about {guess} and it took {c} guesses")


# Add some code to the implementation of
# Newton–Raphson that keeps track of the number of iterations used
# to find the root. Use that code as part of a program that compares the
# efficiency of Newton–Raphson and bisection search. (You should
# discover that Newton–Raphson is far more efficient.)


def bise_newt_comparison(x):
    print(f"With the bisection algorithm these are the results:")
    bise_square(x)
    print(f"With the Newton algorithm these are the results:")
    square_newton(x)


# Finger exercise: Write a function is_in that accepts two strings as
# arguments and returns True if either string occurs anywhere in the
# other, and False otherwise. Hint: you might want to use the built-in
# str operator in.


def is_in(first=str, second=str):
    return True if first in second or second in first else False


# Write a function to test is_in

def test_is_in():
    # check if function works properly
    print(f"performing tests, will return True if everything's allright")
    return bool(is_in("sem", "semantica") and is_in("psycho", "psychology") and is_in("wardrobe", "ward") and not is_in(
        "hansel", "gretel"))


# Write a function mult that accepts either one or
# two ints as arguments. If called with two arguments, the function
# prints the product of the two arguments. If called with one argument,
# it prints that argument.

def mult(a, b=None):
    return a * b if b else a


#  Using the algorithm of Figure 3-6, write a
# function that satisfies the specification

def log(x, epsilon, base=int):
    """Assumes x and epsilon int or float, base an int,
    x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon
    of x."""
    lower_bound = 0
    while base ** lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    # Perfom bisection search
    ans = (high + low) / 2
    while abs(base ** ans - x) >= epsilon:
        if base ** ans < x:
            low = ans
        else:
            high = ans
    return print(f"{ans} is close to the log base {base} of {x}")


# Write a lambda expression that has two numeric
# parameters. If the second argument equals zero, it should return
# None. Otherwise it should return the value of dividing the first
# argument by the second argument. Hint: use a conditional
# expression.

lambda x, y: x / y if y != 0 else None


# Finger exercise: Use find to implement a function satisfying the
# specification
def find_last(s, sub):
    """s and sub are non-empty strings
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s"""
    return s.find(sub) if s.find(sub) != -1 else None


# Finger exercise: Write an expression that evaluates to the mean of
# a tuple of numbers. Use the function sum.

def mean(tup=tuple):
    return sum(tup) / len(tup)


# : What does the following code print?
def finger():
    L = [1, 2, 3]
    L.append(L)
    return print(L is L[-1])


def append_val(val, list_1=[]):
    if list_1: list_1 = []  # if this is omitted list won't be empty in the next calls
    list_1.append(val)
    return print(list_1)


# Finger exercise: Write a list comprehension that generates all
# non-primes between 2 and 100.

prime_100 = [x for x in range(2, 100) if all(x % y != 0 for y in range(3, x))]


def prime_list(n):
    return [x for x in range(3, n, 2) if not [a for a in range(2, x) if x % a == 0]]


# Finger exercise: Implement a function satisfying the following
# specification. Hint: it will be convenient to use lambda in the body of
# the implementation.


def power_l1_l2(l1, l2):
    """l1, l2 lists of same length of numbers
    returns the sum of raising each element in l1
    to the power of the element at the same index in L2
    For example, f([1,2], [2,3]) returns 9"""
    return sum(map(lambda x,y: x**y, l1, l2))


# Finger exercise: Implement a function that meets the specification

def get_min(d=dict):
    """d a dict mapping letters to ints
    returns the value in d with the key that occurs first in the alphabet.
    E.g., if d = {x = 11, b = 12}, get_min returns 12."""
    return d[(min(d.keys()))]


# Finger exercise: The harmonic sum of an integer, n > 0, can be
# calculated using the formula . Write a recursive function
# that computes this.

def harmonic(n=int):
    return 1/n + harmonic(n-1) if n != 1 else n/n

def fib(n):
    """assumes  int >= 0
    returns Fibonacci of n"""
    return 1 if n == 0 or n == 1 else  fib(n-1) + fib(n-2)

def test_fib(n):
    for i in range(n+1):
        print(f"fib of {i} is {fib(i)}")


#  When the implementation of fib in Figure 6-3 is
# used to compute fib(5), how many times does it compute the value
# of fib(2) on the way to computing fib(5)?
# 4 times
